#!/bin/bash

# 1. Montar o subvolume principal (@)
mount -o subvol=@ /dev/sda3 /mnt

# 2. Criar os pontos de montagem internos
mkdir -p /mnt/{boot/efi,var/cache,var/log,tmp}

# 3. Montar os subvolumes auxiliares
mount -o subvol=@cache /dev/sda3 /mnt/var/cache
mount -o subvol=@log /dev/sda3 /mnt/var/log
mount -o subvol=@tmp /dev/sda3 /mnt/tmp

# 4. Montando o boot
mount /dev/sda1 /mnt/boot

# acesso ao hardware por meio do chroot
for i in /dev /dev/pts /proc /sys /run; do mount -B $i /mnt$i; done

# Entrando o SO
chroot /mnt
