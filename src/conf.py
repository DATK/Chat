import json

"""url_post = "http://192.168.0.14:5000/API/fr2"
url_get = "http://192.168.0.14:5000/API/fr2rd"
url_chek = "http://192.168.0.14:5000/chek_wrk_host"
id = "db"
"""


def add(ip):
    url_rul=f"{ip}/get/rules"
    url_post = f"{ip}/API/fr2"
    url_get = f"{ip}/API/fr2rd"
    url_reg = f"{ip}/reg/weqff/23rfew"
    url_inp = f"{ip}/in/weqff/23rfew"
    urls = {"pst": url_post, "get": url_get, "reg": url_reg, "in": url_inp,"rl":url_rul}
    with open(r"C:/Users/Public/Documents/urls.txt", "w", encoding="UTF-8") as f:
        json.dump(urls, f)
    return """Succses
Enter to exit"""


def read():
    with open(r"C:/Users/Public/Documents/urls.txt", "r", encoding="UTF-8") as f:
        urls = json.load(f)
    a = urls["pst"]
    b = len(a)
    b -= 8
    return f"Now using this ip: {a[0:b]}"


x = input("Read or input data?(1-read,2-input): ")
if x == "1":
    print(read())
    a = input("....")
else:
    ip = input("Enter IP: ")
    add(ip)
