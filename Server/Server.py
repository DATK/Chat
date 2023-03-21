from flask import Flask, request


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

@app.route("/chek_wrk_host")
def work():
    return "It_is workin"
#chatflsdt.ddns.net

@app.route("/API/fr2/<path:id>", methods=['POST'])
def messeage(id):
    #print(request.json)
    if len(request.json["messange"])>=200:
        add_text_to_file(txt='5uvnryuo"zvЯoxo',file=id+".txt")
    else:
        add_text_to_file(txt=request.json["messange"],file=id+".txt")
    return "Sory, it is not working"


@app.route("/API/fr2rd/<path:id>", methods=["GET"])
def messeage_read(id):
    return read_mes_file(file=id+".txt")


app.run(host="0.0.0.0")
