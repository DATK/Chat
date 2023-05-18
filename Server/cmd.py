import json
from User_object import User
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
    for i in dc:
        if i%3==0:
            print(dc[i])


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
            gtusr()
    except:
        print("Error")
        
while True:
    cmd=input()
    inp(cmd)