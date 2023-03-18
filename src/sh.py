alf = "QWERTYUIOPASDFGHJ(KLZXCVBNMabc\"defghiЙФЯЧЫЦУК.АВСМИПЕНРТЬОГШЩДЛБЮЖЗХЭЪЬjk)lm/nopqr stuvwxy'z1234567)89_йфячыцувсмипакен|ртьогшлб,юдщзжэхъ*-+=*&:;?!@"
cezar_shifr, cezar_un = [], []


def cezar(text, alf=alf, key=2):
    for j in range(len(text)):
        for i in range(len(alf)):
            # print(i,j)
            if text[j]==alf[i]:
                #if text[j]==" ":
                    #text[j]=='|he|re_|prob|el'
                if i + key > len(alf)-1:
                    # print("          ",i,j)
                    cezar_shifr.append(text[j])
                else:
                    # print("                          ",i,j)
                    cezar_shifr.append(alf[i + key])
                    continue
    return ''.join(cezar_shifr)


def cezar_unsc(text, alf=alf, key=2):
    for j in range(len(text)):
        for i in range(len(alf)):
            # print(i,j)
            if text[j] == alf[i]:
                if i + key > len(alf)-1:
                    # print("          ",i,j)
                    cezar_un.append(text[j])
                else:
                    # print("                          ",i,j)
                    cezar_un.append(alf[i - key])
                    continue
    return ''.join(cezar_un)


def cls():
    cezar_shifr.clear()
    cezar_un.clear()
    return cezar_shifr, cezar_un


print(cezar(text="200 slov maxsimum",key=3))