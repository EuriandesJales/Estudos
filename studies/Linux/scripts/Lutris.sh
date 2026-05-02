#!/bin/bash
# versao 0.9

# atualiza as chaves do repositorio o sistema e instala requisitos do lutris e o memso
echo -e "s\ns\ns\ns\ns\ns\ns\ns\ns" | sudo pacman -Syu wine winetricks wine-mono wine_gecko vulkan-icd-loader lib32-vulkan-icd-loader vkd3d lib32-vkd3d gvfs

# Install Lutris
echo -e "s\ns" | sudo pacman -S lutris

