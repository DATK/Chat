from src import send_message as sm
import time
from src import sh
""""


THIS DONT USE
OLD 


"""

cls = sm.Send_ms()

print("Hello in the my chat")




def sign_in_up(name):
    if input("reg(1) or login(2): ") == "1":
        print("Will be use your name...")
        password = input("Enter password")
        cls.reg(name, password)
        print("Sucses")
    else:
        id = input("Enter id: ")
        with open(r"C:\Users\Public\Documents\id.txt", "w", encoding="UTF-8") as f:
            f.write(id)
        password = input("Enter password: ")
        if cls.ins(name, password) == "sc":
            print("sucs")
            while start(id) != False:
                start(id)
        else:
            print("NO")
            input("please restart app: ")
            exit()

def start(id):
    text = input("Input text >>>>>> ")
    text = "_"+name+"_"+"told_>>>"+text
    text_s = sh.cezar(text=text, key=3)
    try:
        cls.send(text=text_s, id=id)
    except:
        print("Try to connetct srver-->")
        time.sleep(7)


name = input("Enter Your Name: ")
sign_in_up(name)
