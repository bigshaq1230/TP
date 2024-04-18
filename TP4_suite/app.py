def formula():
    f = open("PIS.txt","r")
    g = open("PIS_GF.txt","w")
    for i in f:
        m = i.split(",")
        gf = (5* int(m[3]) + int(m[4]) ) *int(m[5])
        g.write(",".join(m[0:3])+","+str(gf)+"\n")

formula()

def classify():
    g = open("PIS_GF.txt","r")
    list = []
    l = []
    for i in g:
        ch = i.strip().split(",")
        l.append(ch)
        list.append(int(ch[3]))
    list.sort(reverse=True)
    print(l)

    for j in range(len(list)):
        index = 0
        while(int(l[index][3]) != list[j]):
            index = index + 1


        x = l[index]
        l[index] = l[j]
        l[j] = x
    g.close()
    g = open("PIS_GF.txt","w")
    for p in l:
        g.write(",".join(p)+"\n")
classify()
