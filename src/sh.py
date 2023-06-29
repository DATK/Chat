alf = "QWERTYUIOPASDFGHJ(KLZXCVBNMabc\"defghiЙФЯЧЫЦУК.АВСМИПЕНРТ\ЬОГ>ШЩДЛБЮЖЗХЭЪjklm/nopqr stuvwxy'z1234567)89_йф0ячыц<увсмипакен|ртогшлб,юдщьзжэхъ*-+=&:;?!@"


def cezar(text, alf=alf, key=2):
    cezar_shifr = []
    for j in range(len(text)):
        for i in range(len(alf)):
            # print(i,j)
            if text[j] == alf[i]:
                # if text[j]==" ":
                # text[j]=='|he|re_|prob|el'
                if i + key > len(alf)-1:
                    # print("          ",i,j)
                    cezar_shifr.append(text[j])
                else:
                    # print("                          ",i,j)
                    cezar_shifr.append(alf[i + key])

    return ''.join(cezar_shifr)


def cezar_unsc(text, alf=alf, key=2):
    cezar_un = []
    for j in range(len(text)):
        for i in range(len(alf)):
            # print(i,j)
            if alf[i] == text[j]:
                if i + key > len(alf)-1:
                    # print("          ",i,j)
                    cezar_un.append(text[j])
                else:
                    # print("                          ",i,j)
                    cezar_un.append(alf[i - key])

    return ''.join(cezar_un)


"""
def dcc(alf):
    dc={}
    for i in range(len(alf)):
        dc[alf[i]]="1"*i
    dc["Q"]="LEN"
    return dc
"""


def hash(pas):
    new_pas = pas
    r = ""
    res = cezar(cezar(cezar(cezar(new_pas, alf=alf, key=6),
                alf=alf, key=3), alf=alf, key=2), alf=alf, key=7)
    dc = {'э': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', '#': '1', 'I': '11', '7': '111', '_': '1111', '}': '11111', '|': '111111', 'ч': '1111111', 'E': '11111111', 'ъ': '111111111', 'y': '1111111111', 'Э': '11111111111', '8': '111111111111', ';': '1111111111111', 'M': '11111111111111', 'п': '111111111111111', 'U': '1111111111111111', 'Д': '11111111111111111', 'С': '111111111111111111', 'л': '1111111111111111111', 'Ё': '11111111111111111111', '0': '111111111111111111111', 'ё': '1111111111111111111111', '4': '11111111111111111111111', 'П': '111111111111111111111111', 'ж': '1111111111111111111111111', 'к': '11111111111111111111111111', 'я':
          '111111111111111111111111111', 'у': '1111111111111111111111111111', '"': '11111111111111111111111111111', 'т': '111111111111111111111111111111', '~':
          '1111111111111111111111111111111', 'p': '11111111111111111111111111111111', 'р': '111111111111111111111111111111111', 'ю': '1111111111111111111111111111111111', 'У': '11111111111111111111111111111111111', 'В': '111111111111111111111111111111111111', 'w': '1111111111111111111111111111111111111', 'г': '11111111111111111111111111111111111111', '*': '111111111111111111111111111111111111111', 'A': '1111111111111111111111111111111111111111', '>': '11111111111111111111111111111111111111111', 'L': '111111111111111111111111111111111111111111', 'б': '1111111111111111111111111111111111111111111', 'N': '11111111111111111111111111111111111111111111', 'u': '111111111111111111111111111111111111111111111', 'o': '1111111111111111111111111111111111111111111111', 'z': '11111111111111111111111111111111111111111111111', 'b': '111111111111111111111111111111111111111111111111', 'k': '1111111111111111111111111111111111111111111111111', 'е': '11111111111111111111111111111111111111111111111111', '?': '111111111111111111111111111111111111111111111111111', '$':
          '1111111111111111111111111111111111111111111111111111', 'T': '11111111111111111111111111111111111111111111111111111', 'W': '111111111111111111111111111111111111111111111111111111', 'e': '1111111111111111111111111111111111111111111111111111111', 'n': '11111111111111111111111111111111111111111111111111111111', 'Ч': '111111111111111111111111111111111111111111111111111111111', 'Ф': '1111111111111111111111111111111111111111111111111111111111', '!': '11111111111111111111111111111111111111111111111111111111111', 'F': '111111111111111111111111111111111111111111111111111111111111', 'з': '1111111111111111111111111111111111111111111111111111111111111', '3': '11111111111111111111111111111111111111111111111111111111111111', 'Y': '111111111111111111111111111111111111111111111111111111111111111', 'Ц': '1111111111111111111111111111111111111111111111111111111111111111', 'Л': '11111111111111111111111111111111111111111111111111111111111111111', ':': '111111111111111111111111111111111111111111111111111111111111111111', 'З': '1111111111111111111111111111111111111111111111111111111111111111111', 'Г': '11111111111111111111111111111111111111111111111111111111111111111111', '<': '111111111111111111111111111111111111111111111111111111111111111111111', 'ф': '1111111111111111111111111111111111111111111111111111111111111111111111', 'ш': '11111111111111111111111111111111111111111111111111111111111111111111111', 'М': '111111111111111111111111111111111111111111111111111111111111111111111111', 'l': '1111111111111111111111111111111111111111111111111111111111111111111111111', '9': '11111111111111111111111111111111111111111111111111111111111111111111111111', 'Z': '111111111111111111111111111111111111111111111111111111111111111111111111111', 'S': '1111111111111111111111111111111111111111111111111111111111111111111111111111', '6': '11111111111111111111111111111111111111111111111111111111111111111111111111111', 'Й': '111111111111111111111111111111111111111111111111111111111111111111111111111111', 'V': '1111111111111111111111111111111111111111111111111111111111111111111111111111111', '{': '11111111111111111111111111111111111111111111111111111111111111111111111111111111', '+': '111111111111111111111111111111111111111111111111111111111111111111111111111111111', '/': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'g': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'j': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'h': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111', '`': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111', '\\': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'х': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', '%': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', '.': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', '№': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'v': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'x': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'Ь': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'd': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'Ю': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'Н': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'И': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', '(': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', '&': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'i': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'Ы': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'X': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', ']': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', '2': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'q': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'r': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', '^': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', '[': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'Е': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', '5': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'й': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'и': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'О': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'Ш': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'ы': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', ' ': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', '-': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'f': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'B': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', '@': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'C': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'H': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'ь': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 's': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'ц': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'm': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'в': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', '1': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'м': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'д': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'a': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'с': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'G': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'Щ': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', "'": '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'Х': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'Q': 'LEN', 'щ': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'Б': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'R': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 't': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'Т': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'о': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'Р': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', ')': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'а': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'K': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', ',': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'Я': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'O': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'А': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'К': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', '=': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'Ъ': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'Ж': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'c': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'D': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'J': '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'P': '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111', 'н': '11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'}
    for i in range(len(res)):
        s = dc[res[i]]
        r += s

    r = r[0:len(r)//2]+"2"
    return r
