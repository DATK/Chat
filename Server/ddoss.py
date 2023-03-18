import requests as r
from random import randint
sp="qazxswedcvffrtgbnhyujm,ki.lop;/'[]"
res=""
while True:
    id=str(sp[randint(0,len(sp)-1)]+sp[randint(0,len(sp)-1)]+sp[randint(0,len(sp)-1)])
    res+=sp[randint(0,len(sp)-1)]
    res*=4
    r.post(f"http://192.168.0.14:5000/API/fr2/{id}", json={'messange': res})
    r1=r.get(f"http://192.168.0.14:5000/API/fr2rd/{id}")
    #print(r1.text)


