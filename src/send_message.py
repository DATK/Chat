import requests as r
from src import conf as cnf

class Send_ms:
    """This class sending message"""

    def __init__(self, server_adres=cnf.url_post):
        self.server_adres = server_adres

    def send(self,text,id):
        r.post(f"{self.server_adres}/{id}", json={'messange': text})

    def chek_work_hsot(self):
        if r.get(cnf.url_chek):
            return True
        else:
            return False
    

