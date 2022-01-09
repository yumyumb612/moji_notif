#!/usr/bin/python

import getpass
import subprocess
from os import getenv, system
from random import choice

import requests

import settings

try:
    api = settings.api
    if api == "random": api = choice(["history", "number_trivia", "cat_fact", "advice"])
    
    if api == "history":
        date = subprocess.check_output(["date", "+%m/%d"])
        date = date.decode("utf-8").replace("\n", "")
        response = requests.get(f"http://numbersapi.com/{date}/date?json")
        history = response.json()["text"]
        system(f"notify-send 'MOJI' '{history}' -t {settings.time} -i {settings.icon_path} & mpv {settings.ringtone_path} --no-terminal &")
    
    elif api == "number_trivia":
        response = requests.get("http://numbersapi.com/random/trivia?json")
        number_trivia = response.json()["text"]
        system(f"notify-send 'MOJI' '{number_trivia}' -t {settings.time} -i {settings.icon_path} & mpv {settings.ringtone_path} --no-terminal &")
    
    elif api == "cat_fact":
        response = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1")
        cat_fact = response.json()["text"]

        system(f"notify-send 'MOJI' '{cat_fact}' -t {settings.time} -i {settings.icon_path} & mpv {settings.ringtone_path} --no-terminal &")
    
    elif api == "advice":
        response = requests.get("https://api.adviceslip.com/advice")
        advice = response.json()["slip"]["advice"]
        system(f"notify-send 'MOJI' '{advice}' -t {settings.time} -i {settings.icon_path} & mpv {settings.ringtone_path} --no-terminal &")
    
    else:
        system(f"notify-send 'MOJI' 'Elo there {getpass.getuser() or 'good sir'}!\nPls consider configuring my settings located within my folder :D\n\n<i><u>~/.config/moji_notif</u></i>' -t 60000 -i {settings.icon_path} & mpv {settings.ringtone_path} --no-terminal &")

except Exception as error:
    print(f"""
    MOJI: OHNOES!1!! Moji got an error!
    MOJI: pls fix
    MOJI: or raise an issue here: https://github.com/yumyumb612/moji_notif/issues\n
    MOJI: dis da error `{error}`
    """)
    system(f"notify-send 'MOJI ENCOUNTERED AN ERROR!1!!' 'Pls tryna run <i><u>~/.config/moji_notif/main.py</u></i> manually to see da error.' -u critical -i {settings.icon_path} &")
