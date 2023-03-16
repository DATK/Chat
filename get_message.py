import requests as r
import time
from src import sh
def reading():
    while True:
        time.sleep(5)
        f=r.get("http://192.168.0.14:5000/API/fr2rd").text
        f1= sh.cezar_unsc(text=f,key=3)
        sh.cls()
        print(">>> ", f1, " <<<")
        print("------------------------------------------")
        
reading()