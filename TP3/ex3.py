def is_palendrome(ch):
    ch2 = ""
    for i in ch :
        if(i == " "):
            continue
        ch2 = ch2+i.lower()

    l = len(ch2)
    for i in range(l//2):
        if (ch2[i] != ch2[l-1-i]):
            return False
    return True



ch = input("donner une chaine: ")
print(is_palendrome(ch))