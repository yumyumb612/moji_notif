#!/bin/bash

cat moji.txt

printf "\n\nMOJI: Elo there $USER!"
printf "\nMOJI: My naem is MOJI :D now am currently trying to install moji_notif and i need sudo to copy my runner in /usr/bin so dat u can run me anywer.\n"
chmod +x moji_notif
sudo cp -f moji_notif /usr/bin/
if [[ -f /usr/bin/moji_notif ]]; then
    printf "\nMOJI: thonks! i just copied moji_notif to /usr/bin"
else
    printf "\nMOJI: i need sudo :c"
    printf "\nMOJI: pls run my install.sh again\n"
    exit 1
fi

rm -rf ~/.config/moji_notif
mkdir ~/.config/moji_notif
cp -rf * ~/.config/moji_notif
printf "\nMOJI: and copied my files in ur ~/.config/moji_notif, u can configure my settings later."

if [[ -d ~/.config/moji_notif ]] && [ "$(ls -A ~/.config/moji_notif)" ] && [[ -f /usr/bin/moji_notif ]]; then
   printf "\nMOJI: yey!! Installed moji_notif successfully. Now try running moji_notif from ur terminal or dmenu."
   printf "\nMOJI: also make sure dat u hav python, dunst or any notification deamon coz i will be using notify-send, and mpv installed in ur system. also u need internet connection."
   printf "\nMOJI: U can uninstall me anytime by just running my uninstall.sh script. ENJOY! :D\n"
else
   printf "\nMOJI: Smthn went wrong, moji_notif was not installed. Pls fix and try again or raise an issue here: <link>\n"
fi

exit 0