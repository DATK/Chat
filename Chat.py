"""I is will be GUI in future"""
import tkinter as tk
from src import send_message as sm
import time
from src import sh
import get_message as gm
cls = sm.Send_ms()


def start():
    text = input("Input text >>>>>> ")
    text = "_"+get_name()+"_"+"told_>>>"+text
    text_s = sh.cezar(text=text, key=3)
    sh.cls()
    try:
        cls.send(text=text_s, id=id)
    except:
        print("Try to connetct srver-->")
        time.sleep(7)


def get_name():
    nm = name.get()
    if nm:
        return nm
    else:
        nm = "Ghost"
        return nm


def get_id():
    ids = id.get()
    if id:
        with open(r"C:\Users\Public\Documents\id.txt", "w", encoding="UTF-8") as f:
            f.write(ids)
    else:
        with open(r"C:\Users\Public\Documents\id.txt", "w", encoding="UTF-8") as f:
            f.write("db")


window = tk.Tk()

window.geometry("800x600+440+100")
id = tk.Entry(window)
name = tk.Entry(window)
tk.Label(window, text="Enter id:").grid(row=0, column=0, stick="we")
tk.Label(window, text="Your name:").grid(row=1, column=0, stick="we")
id.grid(row=0, column=1, stick="we")
name.grid(row=1, column=1, stick="we")
window.columnconfigure(0, minsize=100)
window.columnconfigure(1, minsize=100)
tk.Button(window, text="Send name", command=get_name).grid(row=1, column=2)
tk.Button(window, text="Send id", command=get_id).grid(row=0, column=2)

tk.mainloop()
