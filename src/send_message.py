import requests as r
import json
with open(r"C:/Users/Public/Documents/urls.txt","r",encoding="UTF-8") as fi:
    urls = json.load(fi)

url_post=urls["pst"]



class Send_ms:
    """This class sending message"""

    def __init__(self, server_adres=url_post):
        self.server_adres = server_adres

    def send(self, text, id):
        r.post(f"{self.server_adres}/{id}", json={'messange': text})

