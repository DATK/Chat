alf = "QWERTYUIOPASDFGHJ(KLZXCVBNMabc\"defghiЙФЯЧЫЦУК.АВСМИПЕНРТ\ЬОГШЩДЛБЮЖЗХЭЪjklm/nopqr stuvwxy'z1234567)89_йф0ячыцувсмипакен|ртогшлб,юдщьзжэхъ*-+=&:;?!@"



def cezar(text, alf=alf, key=2):
    cezar_shifr=[]
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
    cezar_un=[]
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





