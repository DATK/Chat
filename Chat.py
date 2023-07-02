from src import send_message as sm
import time
from src import sh
import os
import json


s = sm.Send_ms()


def tmp_files(name, pas):
    with open("tmp.txt", "w", encoding="UTF-8") as f:
        json.dump({"name": name, "password": pas}, f)


def alf():
    with open("./files/alf.txt", "r", encoding="UTF_8") as f:
        alfa = f.read()
    return alfa


def chat(name, password, rls):
    with open(r"C:\Users\Public\Documents\rl.txt", "w", encoding="UTF-8") as f:
        f.write(str(rls["READ"]))
    if rls["WRITE"] == True:
        id = input("Enter id: ")
        with open(r"C:\Users\Public\Documents\id.txt", "w", encoding="UTF-8") as f:
            f.write(id)
        textrt = "1"
        while textrt != "/exit":
            text = input("Input text >>>>>> ")
            textrt = text
            text = "_"+name+"_"+"told_>>>"+text
            text_s = sh.cezar(text=text, key=3, alf=alf())
            try:
                s.send(text=text_s, id=id, name=name, password=password)
            except:
                print("Try to connetct srver-->")
                time.sleep(5)
    else:
        print("You can't write messange")
        input()


def change(name, password, js):
    json = {"name": name, "password": password, "move": js}
    return s.funcs(json)


def menu(name, password):
    rls = chek_rules(name, password)
    print("""1. Чат
2. Сменить логин(имя)
3. Сменить пароль
4. Удалить аккаунт
5. Повышение прав
6. Выйти из приложения""")
    c = input("Enter number(or '/exit' to quit): ")
    if c == "1":
        chat(name, password, rls)
    elif c == '2':
        a = input("Уверены(yes/no):")
        if a == "yes" or a == "y" or a == "yea":
            name_n = input("Введите новый логин: ")
            js = {"name": name_n}
            print(change(name, password, js))
            name = name_n
            tmp_files(name, password)
            input("Вернутся в меню>>> ")
    elif c == "3":
        a = input("Уверены?(yes/no): ").lower()
        if a == "yes" or a == "y" or a == "yea":
            password_n = input("Введите новый пароль: ")
            password_n = sh.hash(password_n)
            js = {"password": password}
            print(change(name, password, js))
            password = password_n
            tmp_files(name, password)
            input("Вернутся в меню>>> ")
    elif c == "4":
        a = input("Уверены?(yes/no): ").lower()
        if a == "yes" or a == "y" or a == "yea":
            js = {"del": True}
            print(change(name, password, js))
            input("Вернутся в меню>>> ")
            os.system('CLS')
            vhod()
    elif c == "5":
        a = input("""1. READ
2. WRITE
3. READ_WRITE: """)
        if a == "1":
            js = {"READ": True}
            print(change(name, password, js))
        elif a == "2":
            js = {"WRITE": True}
            print(change(name, password, js))
        elif a == "3":
            js = {"R_W": True}
            print(change(name, password, js))
        else:
            print("1 или 2 или 3")
        input("Вернутся в меню>>> ")
    elif c == "6":
        input("Нажмите Ентер")
        exit()
    os.system('CLS')
    menu(name, password)
    return c

def read_ip():
    with open(r"C:/Users/Public/Documents/urls.txt", "r", encoding="UTF-8") as f:
        urls = json.load(f)
    a = urls["pst"]
    b = len(a)
    b -= 8
    return f"Now using this ip: {a[0:b]}"

def add(ip):
    url_rul = f"{ip}/get/rules"
    url_post = f"{ip}/API/fr2"
    url_get = f"{ip}/API/fr2rd"
    url_reg = f"{ip}/reg/weqff/23rfew"
    url_inp = f"{ip}/in/weqff/23rfew"
    url_fn = f"{ip}/chng/qwdas/2312/fewsd33/s"
    urls = {"pst": url_post, "get": url_get, "reg": url_reg,
            "in": url_inp, "rl": url_rul, "fn": url_fn}
    with open(r"C:/Users/Public/Documents/urls.txt", "w", encoding="UTF-8") as f:
        json.dump(urls, f)
    return """Succses
Enter to exit"""


def chek_rules(name, password):
    return s.get_rl(name, password)


def vhod():
    q = input("""1. Регистрация
2. Войти в аккаунт
3. Посмотреть адрес сервера
4. Ввести адрес серверв
>>> """)
    if q == "1":
        name = input("Введите логин: ")
        password = input("Введите пароль: ")
        password = sh.hash(password)
        print(s.reg(name, password))
        print("#######################")
        input("Нажмите Ентер")
        os.system('CLS')
        vhod()
    elif q == "2":
        name = input("Введите логин: ")
        password = input("Введите пароль: ")
        password = sh.hash(password)
        if s.ins(name, password) == "sc":
            os.system('CLS')
            tmp_files(name, password)
            menu(name, password)
        else:
            input("Пароль или логин с ошибкой...")
            os.system('CLS')
            vhod()
    elif q=="3":
        print(read_ip())
        input("Нажмите Ентер")
        vhod()
    elif q=="4":
        ip=input("Введите ip >>> ")
        add(ip)
        os.system('CLS')
        vhod()
    else:
        os.system('CLS')
        vhod()


vhod()
