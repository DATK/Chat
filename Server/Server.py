from flask import Flask, request
from User_object import User


def read_mes_file(file="db.txt"):
    with open(file, "r", encoding="UTF-8") as f:
        txt = f.read()
    return txt


def add_text_to_file(file="db.txt", txt=""):
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
    else:
        return "Another name"
    return "Sucs"


@app.route("/in/weqff/23rfew", methods=['POST', "GET"])
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
    if len(request.json["messange"]) >= 200:
        add_text_to_file(txt='5uvnryuo"zvЯoxo', file=id+".txt")
    else:
        add_text_to_file(txt=request.json["messange"], file=id+".txt")
    return "Sory, it is not working"


@app.route("/get/rules", methods=['POST'])
def rl():
    name = request.json["name"]
    password = request.json["password"]
    usr = User(name=name, password=password)
    return usr.rules_s()


@app.route("/API/fr2rd/<path:id>", methods=["GET"])
def messeage_read(id):
    return read_mes_file(file=id+".txt")


app.run(host="0.0.0.0", debug=True)
