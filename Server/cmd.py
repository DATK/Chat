import json
from User_object import User
import os
import requests as r
import sys
sys.path.insert(1, 'D:\chat_flaks\src')
import sh
def change_rl(name,rl):
    try:
        znach=input("True or False: ")
        if znach.lower()=="true":
            znach=True
        elif znach.lower()=="false":
            znach=False
        u=User(name=name)
        u.change_rules(role=rl,znach=znach)
    except:
        print("Error")

def gtusr():
    with open("db_users_bcp.json","r",encoding="UTF-8") as f:
        dc=json.load(f)
    dcr=[]
    for i in dc:
        if i[:6]=="name__":
            dcr.append(dc[i])
        else:
            continue
    return dcr

def delusr():
    name=input("Enter name: ")
    usr=User(name=name)
    usr.del_user()

def inp(cmd):
    try:
        if cmd=="/rls":
            name=input("Enter name: ")
            rl=input("Enter rule: ").upper()
            change_rl(name,rl)
        elif cmd=="/getrls":
            name=input("Enter name: ")
            u=User(name=name)
            print(u.rules_s())
        elif cmd=="/getusers":
            rs=gtusr()
            for i in range(len(rs)):
                print(f"{i+1}. {rs[i]}")
        elif cmd=="/deluser":
            delusr()
        elif cmd=="/ids":
            path = os.chdir("./ids")
            with os.scandir(path) as listOfEntries:  
                for entry in listOfEntries:
                    if entry.is_file():
                        print(entry.name[:-4])
                        
        elif cmd=="/getmes":
            id=input("Enter id: ")
            a=r.get(f"http://localhost:5000/API/fr2rd/{id}").text
            print(sh.cezar_unsc(text=a,key=3))  
    except:
        print("Error")
        
while True:
    cmd=input()
    inp(cmd)