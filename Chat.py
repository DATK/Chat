from src import send_message as sm
import time
from src import sh

s = sm.Send_ms()


def reg():
    print("------------------REG----------------")
    name = input("Enter yor name: ")
    password = input("Enter password: ")
    password = sh.cezar(text=password, key=5)
    s.reg(name, password)
    print("------------------REG----------------")


def chek_rules(name,password):
    return s.get_rl(name,password)


def work(name,password):
    ruls=chek_rules(name,password)
    with open(r"C:\Users\Public\Documents\rl.txt", "w", encoding="UTF-8") as f:
            f.write(str(ruls["READ"]))
    if ruls["WRITE"]==True:
        id = input("Enter id: ")
        with open(r"C:\Users\Public\Documents\id.txt", "w", encoding="UTF-8") as f:
            f.write(id)
        textrt="1"
        while textrt!="/exit":
            text = input("Input text >>>>>> ")
            textrt=text
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
        print("sucs")
        work(name,password)
    else:
        print("bad")
        
    
def menu():
    print("""1. Registration
2. Login in and start chat""")
    c=input("Enter number(or '/exit' to quit): ")
    if c=="1":
        reg()
    elif c=="2":
        inp()
    return c



def main_loop():
    while menu()!="/exit":
        menu()
    input("Bye")


main_loop()
