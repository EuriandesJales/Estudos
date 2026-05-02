# Base oficial do Kali Linux
FROM kalilinux/kali-rolling 
# Evita prompts interativos do apt
ENV DEBIAN_FRONTEND=noninteractive 

# Atualiza e instala GUI + ferramentas
RUN apt update && apt install -y \
    kali-linux-default \
    xfce4 xfce4-goodies \
    # tightvncserver é um servidor VNC leve para acesso remoto rendeização GUI
    tightvncserver \
    # noVNC é uma interface web para VNC que permite acesso via navegador
    novnc websockify \
    dbus-x11 \
    x11-xserver-utils \
    sudo 
    # && apt clean # Limpa cache do apt para reduzir a imagem

# Cria usuário não-root (boa prática)
RUN useradd -m kali && echo "kali:kali" | chpasswd && adduser kali sudo

USER kali
WORKDIR /home/kali

# Configura VNC
RUN mkdir ~/.vnc && \
    echo "kali" | vncpasswd -f > ~/.vnc/passwd && \
    chmod 600 ~/.vnc/passwd

# copia o script de inicialização para o container
COPY startup.sh /home/kali/startup.sh
# da permissão de execução para o script de inicialização
RUN chmod +x /home/kali/startup.sh

# Expondo as portas para VNC (5901) e noVNC (6080) para acesso remoto
EXPOSE 5901 6080

CMD ["./startup.sh"]