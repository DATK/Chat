import requests as r
import json
with open(r"C:/Users/Public/Documents/urls.txt", "r", encoding="UTF-8") as fi:
    urls = json.load(fi)

url_post = urls["pst"]
url_reg = urls["reg"]
url_in=urls["in"]
url_rl=urls["rl"]


class Send_ms:
    """This class sending message"""

    def __init__(self, url_post=url_post, url_reg=url_reg,url_in=url_in,url_rl=url_rl):
        self.url_post = url_post
        self.url_reg = url_reg
        self.url_in=url_in
        self.url_rl=url_rl
    def send(self, text, id):
        r.post(f"{self.url_post}/{id}", json={'messange': text})

    def reg(self, name, password):
        r.post(self.url_reg,json={"name":name,"password":password})

    def ins(self, name, password):
        if r.post(self.url_in,json={"name":name,"password":password}).text=="Sucs":
            return "sc"
        else:
            return "bad"
    
    def get_rl(self,name,password):
        return r.post(self.url_rl,json={"name":name,"password":password}).json()
    
