import requests as r
import time
def reading():
    while True:
        time.sleep(5)
        f=r.get("http://192.168.0.14:5000/API/fr2rd").text
        print("Yoyr Freind talking: ", f)
        print("------------------------------------------")
        
reading()