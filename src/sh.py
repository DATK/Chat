alf = "QWERTYUIOPASDFGHJ(KLZXCVBNMabc\"defghiЙФЯЧЫЦУК.АВСМИПЕНРТЬОГШЩДЛБЮЖЗХЭЪЬjk)lm/nopqrstuvwxy'z1234567)89_йфячыцувсмипакен|ртьогшлб,юдщзжэхъ*-+=*&:;?!@"
cezar_shifr, cezar_un = [], []


def cezar(text, alf=alf, key=2):
    for j in range(len(text)):
        for i in range(len(alf)):
            # print(i,j)
            if text[j] == alf[i]:
                if i + key > len(alf):
                    # print("          ",i,j)
                    continue
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
                if i + key > len(alf):
                    # print("          ",i,j)
                    continue
                else:
                    # print("                          ",i,j)
                    cezar_un.append(alf[i - key])
                    continue
    return ''.join(cezar_un)


def cls():
    cezar_shifr.clear()
    cezar_un.clear()
    return cezar_shifr, cezar_un
