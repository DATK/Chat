import requests as r


class Send_ms:
    """This class sending message"""

    def __init__(self, server_adres="http://192.168.0.14:5000/API/fr2"):
        self.server_adres = server_adres

    def send(self,text):
        r.post(self.server_adres, json={'messange': text})

    def chek_work_hsot(self):
        if r.get("http://192.168.0.14:5000/chek_wrk_host"):
            return True
        else:
            return False
    

