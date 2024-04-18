def enter(f):
    identity_card = input("Enter identity card: ")
    last_name = input("Enter last name: ")
    first_name = input("Enter first name: ")
    group = input("Enter group: ")
    age = input("Enter age: ")
    decision = input("Enter decision (accepted/refused/adjourned): ")
    ch = identity_card + "," + last_name + "," + first_name + "," + group + "," + age + ":" + decision +";"

    f.write(ch+"\n")


def accepeted(f,g):
    ch  = f.readline()
    print(ch)
    while(ch != ""):
        if (ch[ch.index(":")+1:len(ch)-2] == "accepeted") :
            g.write(ch)
        ch = f.readline()


f = open("competition.txt","r")
g = open("accepted.txt","w")
accepeted(f,g)



