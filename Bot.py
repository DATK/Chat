
from src import send_message as s
from random import randint

class BOT():

    def __init__(self, name, password):
        self.snd = s.Send_ms()
        self.password = password
        self.name = name

    def reg(self):
        self.snd.reg(self.name, self.password)
        
    def chek_reg(self):
        if self.snd.ins(self.name,self.password)=="bad":
            self.name=self.change_name()
            self.password=self.change_pas()
            self.reg()
    
    def change_name(self):
        arr="qwertyuioupiasfdghdfkjhlzcxvbnmQWERTYUIOASDFGHJKLZXCVBNMQWERTYUIукенапрчывормоагневсмбрио"
        name = f"{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}"
        js = {"name": self.name, "password": self.password, "move": {"name": name}}
        self.snd.funcs(js)
        self.name = name
        return name

    def change_pas(self):
        arr="qwertyuioupiasfdghdfkjhlzcxvbnmQWERTYUIOASDFGHJKLZXCVBNMQWERTYUIукенапрчывормоагневсмбрио"
        password = f"{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}"
        js = {"name": self.name, "password": self.password,
              "move": {"password": password}}
        self.snd.funcs(js)
        self.password = password
        return password

    def write(self):
        alf="qwertyuiopodsfgfhjklj;kzxvcbnm,.m/,1243576890QWERTYUIOPIOPOIGHDGDFASFXCVBNQWERTYTUIYUOцукенгешнщгшзщрпраопвпасмиюттРНЕУКЦУЙКЕУНКГЕШНЩГЛОРПЧАСМИОЛТ"
        sms_len=randint(0,150)
        sms=""
        for j in range(sms_len):
            sms+=alf[randint(0,len(alf)-1)]
        id="bot"
        for i in range(randint(0,200)):
            self.snd.send(sms,id,self.name,self.password)
        return sms
    

def test():
    from time import sleep
    arr = "qewrteyuiouplkkjhjghgfdfsddadxvbcvnmbknlkWERTYUOIPIOPKLJKHJGFDFSDFXCVHBKJ"
    name = f"{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}"
    password = f"{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}{arr[randint(0,len(arr)-1)]}"
    bot=BOT(name,password)
    bot.reg()
    x=int(input("Введите задержку(В секундах):"))
    while True:
        bot.chek_reg()
        sms="sms"
        move=randint(1,3)
        if move==1:
            name=bot.change_name()
        elif move==2:
            password=bot.change_pas()
        elif move==3:
            sms=bot.write()
        print(f"""name:{name}

move: {move}
password:{password}
sms: {sms}
###############################""")
        sleep(x)
        
test()
