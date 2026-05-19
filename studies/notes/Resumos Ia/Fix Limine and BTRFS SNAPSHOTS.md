
## O Diagnóstico: O que gerou o erro de E/S?

O erro `Erro de E/S (.snapshots is not a btrfs subvolume)` aconteceu por um **conflito de metadados** entre o espaço de usuário (o programa Snapper) e o espaço de disco (o sistema de arquivos Btrfs).

```
Sua Raiz Atual (@root)
  └── /.snapshots  <── O Snapper tentava ler isto como um SUBVOLUME...
                         ...mas no disco era apenas uma PASTA COMUM ou LINK QUEBRADO.
```

O Snapper possui um arquivo de configuração que dita: _"Para gerenciar a raiz `/`, existe um subvolume Btrfs montado em `/.snapshots`"_. Quando você executava qualquer comando do Snapper, o software fazia uma chamada de sistema (_system call_) para ler esse caminho. O Kernel Linux (VFS) interceptava a chamada e respondia: _"O caminho `/.snapshots` existe, mas ele é uma pasta comum/vazia, não um subvolume Btrfs"_.

Como o Snapper não sabe lidar com esse estado corrompido, ele entrava em pânico e abortava a operação com a mensagem genérica de **Erro de E/S (Input/Output Error)**.

---

## 2. A Origem do Problema (Causa Raiz)

A origem do problema remonta ao momento em que você fez a manutenção do seu sistema e **renomeou o seu subvolume raiz antigo para `@_antigo`** para instalar/substituir pelo **`@root` atual**.

Ao analisar a tabela de subvolumes com o `lsblk` e `btrfs subvolume list`, descobrimos a seguinte árvore estrutural no seu disco `/dev/sdb3`:

Plaintext

```
Top Level 5 (Raiz Absoluta do Disco)
├── @root (ID 257) ─── [Seu sistema operacional ativo hoje]
│     └── /.snapshots (Pasta comum vazia que quebrou o Snapper)
└── @_antigo (ID 256) ─ [Seu sistema antigo abandonado]
      └── .snapshots (ID 264) ─── [O SUBVOLUME REAL DE SNAPSHOTS]
            ├── /22/snapshot (ID 286)
            ├── /23/snapshot (ID 287)
            └── ... (Mais 50 subvolumes filhos)
```

### O nó cego da arquitetura:

Os seus snapshots reais (do ID 22 ao 71) ficaram **órfãos** dentro do subvolume `@_antigo`. Quando você mudou para o `@root`, o Snapper do novo sistema tentou ler a configuração antiga, mas o subvolume `.snapshots` real não veio junto; ele ficou preso no passado.

Por isso, quando tentamos dar o comando `snapper create-config /`, o Snapper acusava que a configuração já existia (porque os arquivos de configuração em `/etc/` ainda estavam lá), mas o subvolume no disco não correspondia à realidade.

---

## 3. Resumo do que já tentamos fazer (E por que falhou)

- **Tentativa 1: Apagar a configuração via Snapper (`delete-config`)**
    
    - _Por que falhou:_ O Snapper travava no erro de E/S antes de aceitar deletar a si mesmo.
        
- **Tentativa 2: Apagar a pasta `/.snapshots` no sistema atual**
    
    - _Por que falhou:_ Tratamos o problema como se fosse apenas uma pasta comum no espaço de usuário, mas o Snapper continuava detectando a duplicidade nos arquivos internos e o Btrfs continuava com os subvolumes antigos intactos no disco.
        
- **Tentativa 3: Deletar o subvolume pai `@_antigo` diretamente no Top Level 5**
    
    - _Por que falhou:_ O Btrfs possui uma regra rígida de segurança: **um subvolume pai não pode ser deletado se contiver subvolumes filhos dentro dele**. Como o `@_antigo` continha os subvolumes dos snapshots e os subvolumes do systemd (`machines` e `portables`), o comando foi rejeitado com o erro `Directory not empty`.
        

---

## 4. O Plano de Ação Daqui para Frente

Para resolver isso de forma limpa e definitiva, sem "gambiarras", precisamos seguir o fluxo correto do Btrfs: **destruir a árvore antiga de baixo para cima** e permitir que o Snapper reconstrua a árvore nova.

O plano consiste em:

1. **Montar a Raiz Absoluta (`/dev/sdb3`) no ID 5** (onde podemos ver todos os subvolumes de fora).
    
2. **Passar a limpeza reversa no `@_antigo`**: Deletar primeiro os subvolumes filhos (`machines`, `portables` e os `snapshots` numéricos) para só então deletar o subvolume pai `@_antigo`. Isso vai liberar espaço em disco e limpar a tabela do sistema.
    
3. **Limpar o espaço de usuário**: Apagar os registros manuais em `/etc/snapper/` para o Snapper esquecer que o `root` já existiu.
    
4. **Criar a nova estrutura**: Rodar o `snapper create-config /` para que o Snapper crie um subvolume limpo e saudável atrelado ao seu `@root` atual.
    
5. **Sincronizar o Bootloader**: Rodar o `limine-snapper-sync` para limpar o menu do Limine de qualquer resquício desses snapshots antigos.
    

Estamos com o mapa completo e os conceitos de subvolumes alinhados. Quando estiver pronto para executar a limpeza no `/dev/sdb3`, me avise.

### 5. O Procedimento de Correção Executado (A Resolução)

Para desatar o nó estrutural, o ecossistema de subvolumes do Btrfs foi manipulado de baixo para cima (da folha para a raiz), seguido da reconfiguração do espaço de usuário.

```
[Top Level 5] ──> Deletar Filhos (machines/portables/snapshots) ──> Deletar Pai (@_antigo)
                                                                            │
[Novo Menu Limine] <── Sincronizar (limine-snapper-sync) <── Criar Config ──┘
```

#### Passo 1: Isolamento e Acesso ao Top Level 5

Bash

```
sudo mkdir -p /mnt/btrfs_root
sudo mount -o subvolid=5 /dev/sdb3 /mnt/btrfs_root
```

- **O que faz:** Cria um diretório temporário e monta a partição do sistema (`/dev/sdb3`) especificando o `subvolid=5`.
    
- **Por que:** O Linux inicializa dentro do subvolume `@root`, o que restringe a visão dos demais subvolumes. Montar o ID 5 (a raiz absoluta do disco) permite enxergar, mover e deletar os subvolumes `@_antigo` e `@root` de forma externa e segura.
    

#### Passo 2: Expurgando os Subvolumes Ocultos do Systemd

Bash

```
sudo btrfs subvolume delete /mnt/btrfs_root/@_antigo/var/lib/portables
sudo btrfs subvolume delete /mnt/btrfs_root/@_antigo/var/lib/machines
```

- **O que faz:** Deleta cirurgicamente os subvolumes internos criados pelo gerenciador de containers do systemd (`nspawn`).
    
- **Por que:** O Btrfs impede estritamente a deleção de um subvolume pai se ele contiver qualquer subvolume filho atrelado. Estes dois diretórios eram heranças ocultas do sistema antigo que bloqueavam a remoção do bloco principal.
    

#### Passo 3: O Laço de Deleção Reversa (Vassoura Btrfs)

Bash

```
for snap in /mnt/btrfs_root/@_antigo/.snapshots/*/snapshot; do
    if [ -d "$snap" ]; then sudo btrfs subvolume delete "$snap"; fi
done

for snap_dir in /mnt/btrfs_root/@_antigo/.snapshots/*; do
    if [ -d "$snap_dir" ]; then
        sudo btrfs subvolume delete "$snap_dir" 2>/dev/null || sudo rm -rf "$snap_dir"
    fi
done

sudo btrfs subvolume delete /mnt/btrfs_root/@_antigo/.snapshots
```

- **O que faz:** Um loop em shell que varre a árvore do `@_antigo`, localiza cada um dos mais de 50 subvolumes de snapshots numéricos, deleta os dados internos (o primeiro `for`), remove as pastas organizadoras (o segundo `for`) e extingue o subvolume pai `.snapshots`.
    
- **Por que:** Força a destruição sequencial da árvore de subvolumes de dentro para fora, liberando o espaço físico em disco no SSD e limpando a tabela de alocação do Btrfs.
    

#### Passo 4: Destruição do Subvolume Pai Órfão

Bash

```
sudo btrfs subvolume delete /mnt/btrfs_root/@_antigo
sudo umount /mnt/btrfs_root
```

- **O que faz:** Deleta o subvolume raiz do sistema antigo (agora completamente vazio) e desmonta a área técnica.
    
- **Por que:** Conclui a limpeza física do disco, removendo o `@_antigo` de forma definitiva e liberando o espaço de armazenamento para o sistema atual.
    

#### Passo 5: Reset do Espaço de Usuário e Criação da Nova Estrutura Healthy

Bash

```
sudo rm -rf /.snapshots
sudo rm -f /etc/snapper/configs/root
echo "" | sudo tee /etc/snapper/configs > /dev/null 2>&1

sudo snapper create-config /
```

- **O que faz:** Remove o diretório fantasma `/.snapshots` do sistema ativo, elimina os arquivos de configuração corrompidos que geravam o erro `config already exists` e instrui o Snapper a gerar uma configuração do zero para o ponto `/`.
    
- **Por que:** Ao encontrar o terreno limpo no disco e nas configurações, o Snapper cria com sucesso o novo subvolume saudável `.snapshots` (ID 337) aninhado diretamente abaixo do seu sistema atual (`@`), restabelecendo a arquitetura correta exigida pelo Btrfs.
    

#### Passo 6: Alinhamento do Limine Bootloader

Bash

```
sudo limine-snapper-sync
```

- **O que faz:** Dispara o script de sincronização automatizada do CachyOS.
    
- **Por que:** Lê a nova tabela de subvolumes limpa, remove todas as entradas de boot antigas (IDs 22 a 71) que apontavam para o `@_antigo` (e que gerariam _Kernel Panic_ se selecionadas) e prepara o menu do Limine para receber os novos snapshots legítimos gerados daqui para frente.