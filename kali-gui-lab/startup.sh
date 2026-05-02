#!/bin/bash

# Inicia VNC server
# display :1, resolução 1280x720, profundidade de cor 24 bits
vncserver :1 -geometry 1280x720 -depth 24

# Inicia noVNC (web interface)
websockify --web=/usr/share/novnc/ 6080 localhost:5901