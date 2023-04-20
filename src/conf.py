import json

"""url_post = "http://192.168.0.14:5000/API/fr2"
url_get = "http://192.168.0.14:5000/API/fr2rd"
url_chek = "http://192.168.0.14:5000/chek_wrk_host"
id = "db"
"""


def add(url_post, url_get):
    url_post = f"{url_post}/API/fr2"
    url_get = f"{url_get}/API/fr2rd"
    urls = {"pst": url_post, "get": url_get}
    with open(r"C:/Users/Public/Documents/urls.txt", "w", encoding="UTF-8") as fi:
        json.dump(urls, fi)
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
    add(ip, ip)
