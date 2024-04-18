
def indexof(ch,x):
    for i in range(len(ch)):
        if (ch[i] == x):
            return i
    return -1


def valid_char(q):
    q = q.upper()
    special = [".","_","+","-"]
    if (("Z"<q or q<"A") and ("9"<q or q<"0") and (indexof(special,q) == -1)):
        return False
    else:
        return True


def valid_email(ch):
    print(ch)
    if len(ch) <5:
        print("too short")
        return False
    if(indexof(ch,"@") == -1):
        print(" @ not found")
        return False
    if(indexof(ch,".") == -1):
        print(" . not found")
        return False
    q = ch[0].upper()
    if (("Z"<q or q<"A") and ("9"<q or q<"0")):
        print("first char should be a num or a letter")
        return False

    alt = indexof(ch,"@")
    point =indexof(ch,".")
    ch1 = ch[1:alt]
    ch2 = ch[alt+1:point]
    ch3 = ch[point+1:]
    chf = ch1+ch2+ch3
    for i in chf:
        for q in i:
            if(valid_char(q) == False):
                print("invalid char: ",q)
                return False
    print("valid email")
    return True
valid_email("asd@gmasacqs.com")

