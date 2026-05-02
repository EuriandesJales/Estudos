## Módulos do curso

1. Primeiros passo HTML+CSS
    
    Conhecimento básico, preparação do ambiente, semântica da HTML5, textos , títulos, ligações, multimidia , estilos.
    
2. Deixando as coisas mais bonitas
    
    Fundamentos do design, psicologia das cores tipografia elementos CSS, modelos de caixas, wireframe, responsividade
    
3. Colocando um protótipo no ar
    
    Versionamento de software, hospedagem de sites estáticos, tabelas.
    
4. Aprofundamento os conhecimentos
    
    quadros em linha, formulários, media queries, mobile first
    
5. Novas tecnologias
    
    flexbox, grid layout, projeto final.
    

## Material Necessário

- Computador
- Celular
- Acesso a internet
- Caderno

## Material de Apoio/Links uteis

[https://github.com/gustavoguanabara/html-css](https://github.com/gustavoguanabara/html-css)

![Referencias](Imagens/Referenicias%20HTML.png)

![[livros desenvolvimento web.png]]

![[livros desenvolvimento web2.png]]

opção 1 se destaca por ser um livro mais teorico

![[livros desenvolvimento web3.png]]

livros de design

### Historia do desenvolvimento da web

No inico foi criado uma pequena rede chamada **ARPANET** com 4 computadores (1969)

devido a variação de funcionamento dos mesmos, foi necessario a criação de um protocolo de transmissão de dados visando a conciestencia da informação, e assim se criou o **MCP.**

Porém, essa rede erá muito limitada pois, para um computador comunicar os outros tinham que parar, somente 1 computador conseguia fazer a transmissão por vez.

**Bob Kaha criou o protocolo TCP e Vint Cerf crilou o protocolo IP**, usamos a junção de ambos os protocolos até hoje geralmente referidos com o protocolo TCP/IP.

Após a expansão desemfreada da ARPANET, foi necessario dividir a mesma em 3 partes

- MILNET (Militar)
- NSFNET (Faculdades)
- COMERCIAS (Existia Varias)

Más, elas queriam conectar-se umas as outras e assim foi criada a **INTERNETNETWORK**, que hoje conhecemos como internet.

ASK INTERNT WORK DOCUMMENTENT:
<iframe width="560" height="315" src="https://www.youtube.com/embed/ITNQsmPf24go&ab_channel=Vox" frameborder="0" allowfullscreen></iframe>
[https://www.youtube.com/watch?v=TNQsmPf24go&ab_channel=Vox](https://www.youtube.com/watch?v=TNQsmPf24go&ab_channel=Vox)

Tim Berners-Lee criou um novo protocolo http:// e assim criando a linguagem HTML, linguagem de marcação de texto, posteriormente criando mais um protocolo o www, Mac andressen criou o primeiro navegador de internet como conhecemos hoje, um interpretador, de HTML

![[www.png]])

Algumas explicações técnicas

## Algumas explicações técnicas

Os endereços IP são dinâmicos, tendo assim uma renovação para garantir mais segurança, porém com saber que é que nessa algazarra❓

DNS: lista de sites indexados com seus respectivos IP atualizados em tempo real, trivial para o funcionamento da internet como conhecemos hoje

![[dns.png]]
O que são Rotas?

as informações são “quebrada” em vários pacotes de bytes para e transmitidas por diferentes trajetórias (Rotas) com o intuito de preservar a privacidade dos dados, dessa forma nenhum computador ou dispositivos possui a totalidade dos bytes a não ser os que envia e o destinatário, as Rotas são o “caminho” pré-determinado a ser utilizado na transferência de cada um desses pequenos pacotes de dados.

Para que o DNS: consiga indicar o IP do servidor é necessário indicar um Domínio

site para adquirir informações sobre o IP:

[https://www.iplocation.net/myip](https://www.iplocation.net/myip)

### URL Significa

**Uniform Resource Locator**, ou **Localizador Uniforme de Recursos** em português. É o endereço usado para localizar recursos na web, como páginas da internet, imagens, vídeos, entre outros.

Uma URL geralmente começa com "http://" ou "https://", seguido pelo nome do domínio (por exemplo, "[google.com](http://google.com)") e pode incluir outras informações, como pastas ou parâmetros de pesquisa.

Exemplo de URL:

`https://www.exemplo.com/pagina.html`

Nesse caso, `https://` é o protocolo, `www.exemplo.com` é o domínio, e `/pagina.html` é o caminho para um arquivo específico na web.

**gTLD** significa **Generic Top-Level Domain** (Domínio de Nível Superior Genérico).

Os **gTLDs** são a parte final de um nome de domínio na internet, depois do ponto, e são usados para categorizar ou classificar os tipos de sites. Os gTLDs não estão associados a um país ou região específica, ao contrário dos **ccTLDs** (Country Code Top-Level Domains), que são ligados a países (como `.br` para o Brasil ou `.us` para os Estados Unidos).

Exemplos de gTLDs incluem:

- **.com** – tradicionalmente usado para sites comerciais.
- **.org** – utilizado por organizações, especialmente sem fins lucrativos.
- **.net** – originalmente destinado a provedores de serviços de rede, mas agora usado de forma geral.
- **.edu** – reservado para instituições educacionais.

Nos últimos anos, muitos novos gTLDs foram lançados, permitindo maior flexibilidade, como **.tech**, **.shop**, **.app**, entre outros. Esses novos domínios ajudam a criar endereços de sites mais específicos e relevantes para diferentes áreas e interesses.

Curiosidade: HTML Geralmete é referido como (a HTML) e CSS como (ás CSS)

pois, HTML referece a linguagem HTML portanto feminino,

e CSS referece as folhas de stilos portanto plural

Curiosidade: o correto é afirmar que você desenvolve em HTML e não “eu programo em HTML”

Glossario:

HTML: Hypertext Markup Languge (linguagem de marcação de texto)

CSS: Cascading Style Sheets (Folhas de stilo em cascata)

## Capítulo 3 Aula 1 Diferença entre HTML CSS E JAVASCRIP

HTML: é todo o conteudo da pagina, iamgem texto, video, audio, hiperlink

um pequeno exemplo da estrutura de um codigo de marcação de texto:

![[strutura css.png]]

CSS: é toda a stetica pagina isso é o design, blocos cores bordas layaut, posições tamanho fontes, sombras, tamanhos ebotões (ao menos a intreface dos mesmos). um exemplo de estruturar de codigo de CSS:

![image.png](attachment:c9f480fa-b2a4-4fa7-8e7c-8c1bffcad13b:image.png)

OBS: Toda declaração em CSS tem ; no final

JAVA: Interações, menu interativos, interações popups, validações

Extenção do Chrome para testar e exemplificar as diferençãs entre as Linguagens:

[https://chromewebstore.google.com/detail/web-developer/bfbameneiokkgbdmiekhjnmfkcnldhhm](https://chromewebstore.google.com/detail/web-developer/bfbameneiokkgbdmiekhjnmfkcnldhhm)

# Estrutura básica de documento HTML

```html
<!DOCTYPE html>
<html lang="pt-br">

    <head>
        <!-- aréa de configurações-->
        <meta charset="UTF-8"> <!--seta codigo de caracteres para UTF-8-->
        <meta name="viewport"
        content="width=device-width",
        initial-scale="1.0">  <!--"Cria" um objeto tamanho de tela e determina que zom del será de 100% ou seja sua totalidade-->
        <title>Olá, Mundo!</title>
    </head>
    <body>
        <!-- Aréa de conteudo do site-->
    </body>
</html>
```

## Front-end e Back end

Font-end: client-side tudo o que o cliente tem acesso, experiencia de usurario, constantemente se une com o trabalho do design

Back-end: trabalha com interações das tecnologias com o servidor comunicação: exemplo de linguagens: PHP JavaScript C# python ruby java

## Direitos autorais de imagem

tudo que tem o intuito de ser monetizado é problematico não levar em conta os direitos autorais do conteudo, pois pode ser não só passivo de processo mais passivo de retirar o conteudo do ar, não somente por a empresa mas até mesmo por a a plataforma, que indentifique isso e remaneje os royaltes gerando com o conteudo.

### Atenção o seu site pode e erá perder rankeamento no google e afins por possuir conteudo autoral não licenciado

# Licenças de Uso de Imagens e Suas Características

Ao utilizar imagens na internet, é essencial entender os diferentes tipos de licenças disponíveis. Usar imagens sem permissão pode gerar penalizações legais e prejudicar o desempenho do seu site em mecanismos de busca. Abaixo, explicamos as principais licenças e suas características.

## 1. **Domínio Público (Public Domain)**

- As imagens estão **livres de direitos autorais**.
- Podem ser usadas para **qualquer propósito**, sem necessidade de atribuição.
- Exemplos: imagens do **Pixabay**, algumas obras antigas.

## 2. **Creative Commons (CC)**

A licença Creative Commons permite o uso gratuito, mas pode ter restrições. Os principais tipos são:

- **CC0 (Creative Commons Zero)**
    - Uso **totalmente livre**, sem necessidade de atribuição.
    - Ideal para projetos comerciais e pessoais.
- **CC BY (Atribuição)**
    - Pode ser usada para qualquer fim, **desde que o autor seja creditado**.
- **CC BY-SA (Atribuição-Compartilha Igual)**
    - Pode ser usada e modificada, **mas a obra derivada deve manter a mesma licença**.
- **CC BY-NC (Atribuição-Não Comercial)**
    - Uso **somente para fins não comerciais**.
    - Requer **crédito ao autor**.
- **CC BY-ND (Atribuição-Sem Derivações)**
    - Pode ser usada, **mas não pode ser modificada**.

## 3. **Licença Royalty-Free (RF)**

- Paga-se **uma vez** pela imagem e pode ser usada múltiplas vezes.
- **Não significa gratuita**, apenas que não há taxas adicionais por uso repetido.
- Bancos de imagens como **Shutterstock, Adobe Stock e iStock** oferecem esse tipo de licença.

## 4. **Direitos Gerenciados (RM - Rights Managed)**

- Licença exclusiva e restritiva.
- Uso específico (exemplo: **apenas para um site, em um país, por um período**).
- Normalmente, **mais cara** que outras licenças.

## 5. **Uso Justo (Fair Use)**

- Permite o uso de imagens protegidas **em certos casos**, como:
    - Educação e pesquisa.
    - Críticas e paródias.
    - Reportagens jornalísticas.
- **Não é uma licença oficial**, e o uso pode ser contestado legalmente.

## 📌 **Dicas para Usar Imagens Legalmente**

✅ Sempre **verifique a licença** antes de usar qualquer imagem.

✅ Se precisar de imagens gratuitas, use bancos como **Unsplash, Pexels e Pixabay**.

✅ Se for criar um site comercial, **considere comprar imagens em bancos pagos**.

✅ Sempre dê **crédito ao autor**, caso a licença exija.

Seguir essas diretrizes garante que seu site esteja em conformidade legal e evita problemas com direitos autorais. 🚀

Links uteis:

- [https://www.pexels.com/pt-br/](https://www.pexels.com/pt-br/)
- [https://unsplash.com/pt-br](https://unsplash.com/pt-br)

## Formatos de Imagens Convencionalmente usados na web

JPEG: funciona atravéz de um algoritimo que agrupa pixeos de cores parecidas ou igual diminuindo a densidade de pixel e dessa forma torando a imagem compacta

PNG: imagem que permite transparencia de fundo

GIF: imagem animada que permite trasparencia de fundo

Webp: criado por a google visando unir as melhores caracteriscas dos formatod de imagem do mercado, como compressão sem perdas, transparencia, animação e compatibilidade

![image.png](attachment:30e11c1a-094c-4002-9aa1-d2e94ba299b2:image.png)

### Uma pequena curiosidade:

### **📌 Por que existem duas versões?**

- Antigamente, o **Windows só permitia extensões de três letras**, então **.jpeg** foi abreviado para **.jpg**.
- No macOS e Linux, **.jpeg sempre foi suportado**.

# O que é Semantica

**Semântica** é o estudo do **significado** das palavras, frases e símbolos em um determinado contexto. No desenvolvimento web, **semântica em HTML** significa usar as tags corretas para dar **significado ao conteúdo**, ajudando navegadores e mecanismos de busca a entenderem o propósito de cada parte da página.

## Porque é importante?

- **Acessibilidade:** Leitores de tela e outras tecnologias assistivas conseguem interpretar o conteúdo corretamente.
- **SEO (Otimização para Mecanismos de Busca):** O Google e outros motores de busca entendem melhor o que é importante na sua página, melhorando a classificação nos resultados de pesquisa.
- **Manutenção e colaboração:** O código fica mais organizado e fácil de entender para outros desenvolvedores.

### Exemplos:

- `<header>`: Cabeçalho da página ou seção.
- `<nav>`: Menu de navegação.
- `<article>`: Conteúdo independente, como uma postagem de blog.
- `<section>`: Agrupamento de conteúdo relacionado.
- `<footer>`: Rodapé da página ou seção.
- **`<strong>`** para **informações importantes**.
- **`<em>`** para **ênfase** ou **expressão emocional**.
- **`<u>`** só quando for **nome próprio** ou **termo especial**.
- <address> indica um endereço

# DICA 💡:

utilize a funcção wwa para envelopar um codigo, isso é colocar um codigo dentro do codigo sem a ncessidade de dar CTRL+X CTRL+V

![[envelopamentovscode.png]]


# SEO 
	é como chama o algoritmo utilizado por mecanismos de buscas para identificar e indexar  o seu site

