import requests as r
from src import sh
import time
import json



with open(r"C:/Users/Public/Documents/urls.txt", "r", encoding="UTF-8") as fi:
    urls = json.load(fi)

url_get = urls["get"]

with open(r"C:\Users\Public\Documents\id.txt", "r", encoding="UTF-8") as f:
    id = f.read()

url_id = f"{url_get}/{id}"


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

if __name__=="__main__":
    reading()
