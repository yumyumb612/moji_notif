#!/usr/bin/python

import getpass
import subprocess
from os import getenv, system
from random import choice

import requests

import settings

try:
    api = settings.api
    api_list = ["history", "number_trivia", "cat_fact", "advice"]
    if api == "random": api = choice(api_list)
    def notify(text: str):
        system(f"notify-send 'MOJI' '{text}' -t {settings.time} -i {settings.icon_path} & mpv {settings.ringtone_path} --no-terminal &")
    
    if api == "history":
        date = subprocess.check_output(["date", "+%m/%d"])
        date = date.decode("utf-8").replace("\n", "")
        response = requests.get(f"http://numbersapi.com/{date}/date?json")
        history = response.json()["text"]
        notify(history)

    elif api == "number_trivia":
        response = requests.get("http://numbersapi.com/random/trivia?json")
        number_trivia = response.json()["text"]
        notify(number_trivia)
    
    elif api == "cat_fact":
        response = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1")
        cat_fact = response.json()["text"]
        notify(cat_fact)
    
    elif api == "advice":
        response = requests.get("https://api.adviceslip.com/advice")
        advice = response.json()["slip"]["advice"]
        notify(advice)
    
    else:
        if api and not api in api_list:
            system(f"notify-send 'MOJI' 'Elo again {getpass.getuser() or 'good sir'}!\nIt seems like <i>{api}</i> isnt in my api options :c\nValue can only be <b><u>history</u>; <u>number_trivia</u>; <u>cat_fact</u>; <u>advice</u>; <u>random</u></b>' -t 60000 -i {settings.icon_path} & mpv {settings.ringtone_path} --no-terminal &")
        else:
            system(f"notify-send 'MOJI' 'Elo there {getpass.getuser() or 'good sir'}!\nPls consider configuring my settings located within my folder :D\n\n<i><u>~/.config/moji_notif</u></i>' -t 60000 -i {settings.icon_path} & mpv {settings.ringtone_path} --no-terminal &")

except Exception as error:
    print(f"""
    MOJI: OHNOES!1!! Moji got an error!
    MOJI: pls fix
    MOJI: or raise an issue here: https://github.com/yumyumb612/moji_notif/issues\n
    MOJI: dis da error
    MOJI: `{error}`
    """)
    system(f"notify-send 'MOJI ENCOUNTERED AN ERROR!1!!' 'Pls tryna run <i><u>~/.config/moji_notif/main.py</u></i> manually from da terminal to see da error.' -u critical -i {settings.icon_path} &")
