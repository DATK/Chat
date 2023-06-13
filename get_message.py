import requests as r
from src import sh
import time
import json

with open(r"C:\Users\Public\Documents\rl.txt", "r", encoding="UTF-8") as f:
    read = f.read()

with open(r"C:/Users/Public/Documents/urls.txt", "r", encoding="UTF-8") as fi:
    urls = json.load(fi)

with open(r"C:\Users\Public\Documents\id.txt", "r", encoding="UTF-8") as f:
    id = f.read()

url_get = urls["get"]
url_id = f"{url_get}/{id}"


def alf():
    with open("./files/alf.txt", "r", encoding="UTF_8") as f:
        alfa = f.read()
    return alfa


def rd_tmp():
    with open("tmp.txt", "r", encoding="UTF-8") as f:
        js = json.load(f)
    return js



def getmes():
    js=rd_tmp()
    try:
        f=r.post(url_id,json=js).text
    except:
        print("No connect, try to connect again")
    f1 = sh.cezar_unsc(text=f, key=3,alf=alf())
    print("### ", f1, " ###")
    time.sleep(3)
    
if __name__=="__main__":
    while True:
        getmes()


