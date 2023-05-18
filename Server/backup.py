import json
from time import sleep
def read():
    try:
        with open("db_users.json","r",encoding="UTF-8") as f:
            a=json.load(f)
        with open("db_users_bcp.json","w",encoding="UTF-8") as f:
            json.dump(a,f)
        return "sucs"
    except:
        return "Error"
    
def fix():
    with open("db_users_bcp.json","r",encoding="UTF-8") as f:
        a=json.load(f)
    with open("db_users.json","w",encoding="UTF-8") as f:
        json.dump(a,f)
     
import time
while True:
    if read()=="Error":
        fix()
    time.sleep(2)
    