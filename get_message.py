import requests as r
import time
from src import conf as cnf
from src import sh

with open("C:/Users/Documents", "r", encoding="UTF-8") as f:
    id = f.read()
url_id=f"{cnf.url_get}/{id}"


def reading():
    while True:
        time.sleep(5)
        try:
            f = r.get(url_id).text
        except:
            print("No connect, try to connect again")
            continue
        f1 = sh.cezar_unsc(text=f, key=3)
        sh.cls()
        print("### ", f1, " ###")
        print("------------------------------------------")


reading()
