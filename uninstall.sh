#!/bin/bash

cat moji.txt
printf "\n\nMOJI: Elo again $USER!"
printf "\nMOJI: Am about to uninstall moji_notif and i need sudo to remove my runner from /usr/bin\n"
if [[ -f /usr/bin/moji_notif ]]; then
    sudo rm /usr/bin/moji_notif
fi
if [[ ! -f /usr/bin/moji_notif ]]; then
    printf "\nMOJI: thonks! i just yeeted moji_notif from /usr/bin"
else
    printf "\nMOJI: i need sudo :c"
    printf "\nMOJI: pls run my uninstall.sh again\n"
    exit 1
fi

rm -rf ~/.config/moji_notif

if [[ ! -d ~/.config/moji_notif ]] && [[ ! -f /usr/bin/moji_notif ]]; then
   printf "\nMOJI: Just uninstalled moji_notif. HAB A GOOOD ONE!"
   printf "\nMOJI: Keep safe and stay haaaaaaaaaaaaaaaaaaaaappy <3\n"
else
   printf "\nMOJI: Smthn went wrong, moji_notif was not uninstalled. Pls fix and try again or raise an issue here: <link>\n"
fi

exit 0