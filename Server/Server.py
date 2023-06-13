from flask import Flask, request
from User_object import User


def read_mes_file(file="./ids/db.txt"):
    with open(file, "r", encoding="UTF-8") as f:
        txt = f.read()
    return txt


def add_text_to_file(file="./ids/db.txt", txt=""):
    with open(file, "w", encoding="UTF-8") as f:
        f.write(txt)


def clear(file="db.txt"):
    with open(file, "w", encoding="UTF-8") as f:
        f.write("")


app = Flask(__name__)


@app.route("/")
def wo():
    return "It_is workin"


@app.route("/reg/weqff/23rfew", methods=['POST'])
def reg():
    name = request.json["name"]
    password = request.json["password"]
    usr = User(name=name, password=password)
    if usr.chek_usr() == True:
        usr.add_to_db()
        return "Sucs"
    else:
        return "Zanyato"
    


@app.route("/in/weqff/23rfew", methods=['POST'])
def inp():
    name = request.json["name"]
    password = request.json["password"]
    usr = User(name=name, password=password)
    if usr.chek_usr() == False:
        if usr.chek_user() == True:
            return "Sucs"
        else:
            return "bad"
    else:
        return "bad"


@app.route("/API/fr2/<path:id>", methods=['POST'])
def messeage(id):
    # print(request.json)
    name = request.json["name"]
    password = request.json["password"]
    text=request.json["messange"]
    usr = User(name=name, password=password)
    if usr.chek_user() == True:
        if usr.rules_s()["WRITE"]==True:
            if len(text) >= 501:
                add_text_to_file(txt='brwuorthu)ыыunhwwhtv', file=f"/ids/{id}.txt")
            else:
                add_text_to_file(txt=text, file=f"./ids/{id}.txt")
            return "Sory, it is not working"
        else:
            return "Cant write"
    else:
        return "no this user"


@app.route("/get/rules", methods=['POST'])
def rl():
    name = request.json["name"]
    password = request.json["password"]
    usr = User(name=name, password=password)
    return usr.rules_s()


@app.route("/API/fr2rd/<path:id>", methods=["POST"])
def messeage_read(id):
    name=request.json["name"]
    password = request.json["password"]
    usr=User(name=name,password=password)
    if usr.chek_user() == True:
        if usr.rules_s()["READ"]==True:
            return read_mes_file(file=f"./ids/{id}.txt")
        else:
            return ""
    else:
        return ""


@app.route("/chng/qwdas/2312/fewsd33/s", methods=['POST'])
def chng():
    js = request.json
    usr = User(js["name"], js["password"])
    if usr.chek_usr() == False:
        if "del" in js["move"]:
            usr.del_user()
            return "Delete sucs"
        else:
            return usr.fc(js["move"])
    else:
        return "No this user"


app.run(host="0.0.0.0", debug=True)
