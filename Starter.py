from src import send_message as gm
import subprocess

#subprocess.call("cm.bat")

cls=gm.Send_ms()


print("Hello in the my chat")


st = input("Do you want to connect(yes or no): ")


def start():
    if cls.chek_work_hsot()==True:
        text=input("Введите ваше сообщение... ")
        cls.send(text)
        return True
    else:
        print("Sory, host is dont working")
        return False
        
    
if st.lower()=="yes":
    tmp=input("Запустите пожалуйса файл read.exe для чтения записей, спасибо")
    while start()!=False:
        start()
else:
    print("stoping... ")