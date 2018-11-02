def encrypt(offset, text):
    str_A = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    srt_a = ('abcdefghijklmnopqrstuvwxyz')
    lst_A = list(str_A)
    lst_a = list(srt_a)
    lst_new_A = []
    lst_new_a = []
    str_otvet = ''
    if 0 <= offset <= 25:
        for i in range(65, 91):
            lst_new_A.append(chr(i+offset))
            if (i+offset) == 90:
                break
        for i in range(65, 65+offset):
            lst_new_A.append(chr(i))
        for i in range(97, 123):
            lst_new_a.append(chr(i+offset))
            if i+offset == 122:
                break
        for i in range(97, 97+offset):
            lst_new_a.append(chr(i))

    if -25 <= offset <= -1:
        for i in range(91+offset, 91):
            lst_new_A.append(chr(i))
        for i in range(65, 91+offset):
            lst_new_A.append(chr(i))
        for i in range(123+offset, 123):
            lst_new_a.append(chr(i))
        for i in range(97, 123+offset):
            lst_new_a.append(chr(i))
    lst_text = list(text)
    for i in range(len(text)):
        if 65 <= ord(lst_text[i]) <= 90:
            str_otvet += lst_new_A[lst_A.index(lst_text[i])]
        else:
            if 97 <= ord(lst_text[i]) <= 122:
                str_otvet += lst_new_a[lst_a.index(lst_text[i])]
            else:
                str_otvet += lst_text[i]
    return str_otvet


def decrypt(offset, text):
    return encrypt(-offset, text)
