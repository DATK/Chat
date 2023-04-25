from src import send_message as sm
import time
from src import sh
import os


s = sm.Send_ms()


def reg():
    print("------------------REG----------------")
    name = input("Enter yor name: ")
    password = input("Enter password: ")
    password = sh.cezar(text=password, key=5)
    s.reg(name, password)
    print("Sucses reg")
    print("------------------REG----------------")


def chek_rules(name, password):
    return s.get_rl(name, password)


def change(js):
    print("Login in acount>>> ")
    name = input("Enter your name: ")
    password = input("Enter password: ")
    password = sh.cezar(text=password, key=5)
    json = {"name": name, "password": password, "move": js}
    return s.funcs(json)


def work(name, password):
    ruls = chek_rules(name, password)
    with open(r"C:\Users\Public\Documents\rl.txt", "w", encoding="UTF-8") as f:
        f.write(str(ruls["READ"]))
    if ruls["WRITE"] == True:
        id = input("Enter id: ")
        with open(r"C:\Users\Public\Documents\id.txt", "w", encoding="UTF-8") as f:
            f.write(id)
        textrt = "1"
        while textrt != "/exit":
            text = input("Input text >>>>>> ")
            textrt = text
            text = "_"+name+"_"+"told_>>>"+text
            text_s = sh.cezar(text=text, key=3)
            try:
                s.send(text=text_s, id=id)
            except:
                print("Try to connetct srver-->")
                time.sleep(5)
    else:
        print("You can't write messange")
        input()


def inp():
    print("------------------IN----------------")
    name = input("Enter your name: ")
    password = input("Enter password: ")
    print("------------------IN----------------")
    password = sh.cezar(text=password, key=5)
    if s.ins(name, password) == "sc":
        print("Sucses inp")
        work(name, password)
    else:
        print("Password or login not that")


def menu():
    print("""1. Registration
2. Login in and start chat
3. Change your name
4. Change password
5. Delete user
6. Try to up rules""")
    c = input("Enter number(or '/exit' to quit): ")
    if c == "1":
        reg()
        input("Enter to back to menu>>> ")
    elif c == "2":
        inp()
        input("Enter to back to menu>>> ")
    elif c == '3':
        name = input("Enter new name: ")
        js = {"name": name}
        print(change(js))
        input("Enter to back to menu>>> ")
    elif c == "4":
        a = input("Sure?(yes/no): ").lower()
        if a == "yes":
            password = input("Enter new password: ")
            password = sh.cezar(text=password, key=5)
            js = {"password": password}
            print(change(js))
            input("Enter to back to menu>>> ")
    elif c == "5":
        a = input("Sure?(yes/no): ").lower()
        if a == "yes":
            js={"del":True}
            print(change(js))
            input("Enter to back to menu>>> ")
    elif c == "6":
        a=input("""1. READ
2. WRITE
3. READ_WRITE: """)
        if a=="1":
            js = {"READ": True}
            print(change(js))
        elif a=="2":
             js = {"WRITE": True}
             print(change(js))
        elif a=="3":
             js = {"R_W": True}
             print(change(js))
        else:
            print("1 or 2 or 3")
        input("Enter to back to menu>>> ")     
        
    os.system('CLS') 
    return c


def main_loop():
    while menu() != "/exit":
        menu()
    input("Bye")


main_loop()
