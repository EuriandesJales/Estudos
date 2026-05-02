# O que e?
e um software cli que permite o download de videos do youtube
# Manual de Uso do yt-dlp

## Instalação

### Ubuntu/Debian
```bash
sudo apt update && sudo apt install yt-dlp ffmpeg
```

Caso o yt-dlp não esteja disponível nos repositórios, instale manualmente:
```bash
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
```

---

## Comandos Básicos

### 1. Baixar um vídeo
```bash
yt-dlp "URL_DO_VIDEO"
```

### 2. Baixar uma playlist completa
```bash
yt-dlp "URL_DA_PLAYLIST"
```

### 3. Baixar apenas o áudio (MP3)
```bash
yt-dlp -f bestaudio --extract-audio --audio-format mp3 "URL_DO_VIDEO"
```

### 4. Baixar um vídeo em 720p com melhor áudio
```bash
yt-dlp -f "bestvideo[height=720]+bestaudio" --merge-output-format mp4 "URL_DO_VIDEO"
```

---

## Opções Avançadas

### Especificar a pasta de destino
```bash
yt-dlp -o "~/Downloads/%(title)s.%(ext)s" "URL_DO_VIDEO"
```

### Acelerar o download (4 conexões simultâneas)
```bash
yt-dlp -N 4 "URL_DO_VIDEO"
```

### Exibir todas as qualidades disponíveis
```bash
yt-dlp -F "URL_DO_VIDEO"
```

### Baixar legendas (se disponíveis)
```bash
yt-dlp --write-subs --sub-lang en "URL_DO_VIDEO"
```

### Atualizar o yt-dlp
```bash
sudo yt-dlp -U
```

---

## Ajuda e Mais Opções
```bash
yt-dlp --help
```

Para mais informações, acesse: [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp)

