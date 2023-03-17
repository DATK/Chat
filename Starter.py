from src import send_message as gm
import time
from src import sh




cls=gm.Send_ms()

print("Hello in the my chat")

st = input("Do you want to connect(yes or no): ")
name=input("Enter Your Name: ")
id=input("Enter id: ")
input("""Please, start read.exe and Separate with underscore because shifrovanie not ideal
and please dont use symbols : ; ? ! @, because may be error(press Enter) """)
with open("C:/Users/Documents","w",encoding="UTF-8") as f:
    f.write(id)


def start():
    if cls.chek_work_hsot()==True:
        text=input("Input text >>>>>> ")
        text="_"+name+"_"+"told_>>>"+text
        text_s=sh.cezar(text=text,key=3)
        sh.cls()
        try:
            cls.send(text=text_s,id=id)
        finally:
            print("Try to connetct srver-->")
            time.sleep(7)
        return True
    else:
        print("Sory, host is dont working")
        return False
        
    


while start()!=False:
    start()
