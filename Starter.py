from src import send_message as gm
import time
from src import sh


cls = gm.Send_ms()

print("Hello in the my chat")

st = input("Do you want to connect(yes or no): ")
name = input("Enter Your Name: ")
id = input("Enter id: ")
input("""Please, start read.exe and Separate with underscore because shifrovanie not ideal
and please dont use symbols : ; ? ! @, because may be error(press Enter) """)
with open(r"C:\Users\Public\Documents\id.txt", "w", encoding="UTF-8") as f:
    f.write(id)



def start():
    text = input("Input text >>>>>> ")
    text = "_"+name+"_"+"told_>>>"+text
    text_s = sh.cezar(text=text, key=3)
    try:
        cls.send(text=text_s, id=id)
    except:
        print("Try to connetct srver-->")
        time.sleep(7)



while start() != False:
    start()


