line = int(input("numver of lines"))
rows = int(input("numver of rows"))

for i in range(1,line+1):
    ch = ""
    for j in range(1,rows+1):
        ch = ch + str(i*j) + " " 
    print(ch)