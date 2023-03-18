import json

"""url_post = "http://192.168.0.14:5000/API/fr2"
url_get = "http://192.168.0.14:5000/API/fr2rd"
url_chek = "http://192.168.0.14:5000/chek_wrk_host"
id = "db"
"""



url_post=input("Press url to send>>> ")
url_get=input("Press url to get>>> ")
url_post=f"{url_post}/API/fr2"
url_get=f"{url_post}/API/fr2rd"

urls={"pst": url_post,"get": url_get}

with open("C:/Users/Public/Documents/urls.txt","w",encoding="UTF-8") as fi:
    json.dump(urls,fi)
    