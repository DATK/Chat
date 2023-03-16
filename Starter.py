from src import send_message as gm
import subprocess
from src import sh

#subprocess.call("cm.bat")

cls=gm.Send_ms()


print("Hello in the my chat")


st = input("Do you want to connect(yes or no): ")


def start():
    if cls.chek_work_hsot()==True:
        text=input("Input text >>>>>> ")
        text_s=sh.cezar(text=text,key=3)
        sh.cls()
        cls.send(text_s)
        return True
    else:
        print("Sory, host is dont working")
        return False
        
    
if st.lower()=="yes":
    input("""Please, start read.exe and Separate with underscore because shifrovanie not ideal
and please dont use symbols : ; ? ! @, because may be error(press Enter) """)
    while start()!=False:
        start()
else:
    print("stoping... ")