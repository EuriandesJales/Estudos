
---
## 📦O **Nix** é um **gerenciador de pacotes funcional e declarativo**

### Conceito-chave:

- Ele trata pacotes como **funções puras** (sem efeitos colaterais).
    
- Cada pacote é construído em um ambiente **imutável e isolado**.
	    um contêiner, onde cada pacote recebe cada um das suas dependências com as versões necessárias.

📖 **Glossário**

- **Declarativo**: você descreve o estado desejado, não os passos.
- **Imutabilidade**: arquivos não são alterados, apenas substituídos por novas versões.
- **Pureza (Functional)**: mesma entrada → mesma saída (reprodutibilidade garantida).
    

---

### 🧠 O que é o nixpkgs?
	https://search.nixos.org/packages
	
- Um **repositório Git** com milhares de pacotes
- Cada pacote é descrito em **Nix expressions (.nix)**
    

## 🔎 Como descobrir nomes de pacotes

### Método 1 (oficial — CLI moderna)

```
nix search nixpkgs <nome>
```

---

### 🔁 Build System

O Nix usa **derivações (derivations)**:

```nix
derivation {
  name = "meu-pacote";
  builder = "/bin/sh";
}
```

👉 Internamente:

1. Define dependências
    
2. Gera hash
    
3. Build isolado (sandbox)
    
4. Output vai pro `/nix/store`
    

---
## 🔍 Onde os pacotes ficam acessíveis?

Após instalar:
```
~/.nix-profile/bin
```
👉 Isso entra no seu `$PATH`

## 🔄 Atualizar pacotes

nix profile upgrade

## ❌ Remover pacote
```
nix profile remove <nome>
```
---

## 📜 Listar pacotes instalados
```
nix profile list
```
---

# ⚙️ Configuração do Nix (ESSENCIAL)

## 📂 Arquivo principal
```
/etc/nix/nix.conf
```
Ou usuário:
```
~/.config/nix/nix.conf
```
---

## 🔧 Configuração mínima recomendada

experimental-features = nix-command flakes

```
{
  description = "Pacotes pessoais";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs";

  outputs = { self, nixpkgs }:
  let
    system = "x86_64-linux";
    pkgs = import nixpkgs { inherit system; };
  in {
    packages.${system}.default = pkgs.buildEnv {
      name = "my-packages";
      paths = [
        pkgs.git
        pkgs.neovim
        pkgs.htop
        pkgs.tmux
      ];
    };
  };
}
```

### Instalar tudo de uma vez:
```
nix profile install .#
```

---

### 🧠 Modelo mental

| Modelo tradicional         | Modelo Nix       |
| -------------------------- | ---------------- |
| Mutável                    | Imutável         |
| Imperativo (`apt install`) | Declarativo      |
| Conflitos de libs          | Isolamento total |
| Difícil rollback           | Rollback nativo  |
|                            |                  |

---
## ⚖️ Análise Comparativa: Gerenciamento Imutável (Nix)

|**Categoria**|**✅ Vantagens**|**❌ Desvantagens**|
|---|---|---|
|**Operacional**|**Reprodutibilidade total:** O sistema é idêntico em qualquer máquina.|**Curva de aprendizado:** Exige domínio da linguagem funcional Nix.|
|**Segurança**|**Isolamento (Sandbox):** Pacotes não interferem uns nos outros.|**Debug complexo:** Rastrear erros em camadas de abstração é difícil.|
|**Resiliência**|**Rollback instantâneo:** Falhou? Volte para a versão anterior em segundos.|**Uso de disco:** Armazena múltiplas versões no `/nix/store`, consumindo mais espaço.|
|**Desenvolvimento**|**Múltiplas versões:** Rode Python 3.8 e 3.12 simultaneamente sem conflitos.|**Builds lentos:** A compilação ou derivação de pacotes pode demorar mais que binários pré-prontos.|


## 🔄 Diferença: Nix vs Flatpak

|Aspecto|Nix|Flatpak|
|---|---|---|
|Escopo|Sistema inteiro|Apps desktop|
|Modelo|Declarativo|Imperativo|
|Isolamento|Build + runtime|Runtime (sandbox)|
|Reprodutibilidade|Forte|Parcial|
|Uso principal|Infra + dev + OS|Apps GUI|
|Store|`/nix/store`|`/var/lib/flatpak`|


---

## 🛠️ Guia de Instalação

### Multiusuário (padrão enterprise)

```bash
sh <(curl -L https://nixos.org/nix/install) --daemon
```

### O que isso faz:

- Cria daemon `nix-daemon`
    
- Configura `/nix`
    
- Permite múltiplos usuários
    

📌 Pós-instalação:

```bash
source /etc/profile.d/nix.sh
```

---

## ⚙️ Guia de Configuração

### 📂 Arquivo principal

Modo moderno (recomendado):

```
/etc/nix/nix.conf
```

Modo usuário:

```
~/.config/nix/nix.conf
```

---

### 🔧 Habilitar flakes (ESSENCIAL)

```conf
experimental-features = nix-command flakes
```

---

### 📦 Exemplo: instalar pacotes

```bash
nix profile install nixpkgs#htop
nix profile install nixpkgs#git
```

---

### 🧪 Dev environment (flake)

```nix
{
  description = "Dev shell Python";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs";

  outputs = { self, nixpkgs }:
  let
    pkgs = import nixpkgs { system = "x86_64-linux"; };
  in {
    devShells.default = pkgs.mkShell {
      buildInputs = [
        pkgs.python3
        pkgs.git
        pkgs.nodejs
      ];
    };
  };
}
```

Entrar no ambiente:

```bash
nix develop
```

---

### 📦 Apps comuns

```bash
nix profile install nixpkgs#firefox
nix profile install nixpkgs#neovim
nix profile install nixpkgs#docker
nix profile install nixpkgs#tmux
```

---

### como Levar as configs

o arquivo 
```
~/.config/nixpkgs/home.nix
```

usando o **Home Manager**, que é o padrão de mercado para gerenciar dotfiles com Nix
**Moderno (Flakes):** O padrão atual é usar um arquivo chamado `flake.nix`. Ele é mais robusto porque trava as versões exatas de todas as dependências (lockfile), garantindo 100% de reprodutibilidade.

### Onde colocar o arquivo no novo sistema?
Você pode colocar o arquivo em qualquer diretório do seu usuário 
ex: `
```
~/.config/nix/
```

### Como mandar o Nix construir o sistema?
#### Se estiver usando Home Manager (em qualquer SO):

```
home-manager switch
```

#### Se estiver usando Flakes (O padrão "Senior"):

```
nix store gc # Limpeza opcional antes
nixos-rebuild switch --flake .#nome-do-host
```

---


