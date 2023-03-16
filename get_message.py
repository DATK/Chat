import requests as r
import time
from src import conf as cnf
from src import sh


def reading():
    while True:
        time.sleep(5)
        f = r.get(cnf.url_get).text
        f1 = sh.cezar_unsc(text=f, key=3)
        sh.cls()
        print("### ", f1, " ###")
        print("------------------------------------------")


reading()
