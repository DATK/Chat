from src import send_message as gm
import subprocess

subprocess.call("cm.bat")

cls=gm.Send_ms()


print("Hello in the my chat")


st = input("Do you want to connect(yes or no): ")


def start():
    if cls.chek_work_hsot()==True:
        #subprocess.call("read.exe")
        text=input("Введите ваше сообщение... ")
        cls.send(text)
    else:
        print("Sory, host is dont working")
        
    
if st.lower()=="yes":
    while True:
        start()
else:
    print("stoping... ")