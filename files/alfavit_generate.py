from random import randint


def add_to_file(alf):
    with open("./alf_generated.txt","w",encoding="UTF-8") as f:
        f.write(alf)


def generator():
    alf=""
    db="~`1234567890-=+_)(*&^%$#@!№;:?\"\|/qw ertyuiop[]{}'lkjhgfdsazxcvbnm,.><ёйцукенгшщзхъэждлорпавыфячсмитьбюЁЙФЯЧЫЦУВСМАКЕПИТРНГОЬБЛШЩДЮЗЖЭХЪPOIUYTREWQZCXBVNMASDFGLKJH"
    a=0
    i=0
    b=len(db)-1
    while i <= b:
        tmp=randint(a,b)
        s=db[tmp]
        if s in alf:
            continue
        else:
            i+=1
            alf+=s
        
    return alf

add_to_file(generator())