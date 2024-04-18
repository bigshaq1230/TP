def counter(start,stop):
    ch = ""
    x = start
    y = stop
    if(x > y):
        ch = ch + "counting down "
        for i in range(y,x+1):
            ch = ch + str(x) + " "
            x = x - 1

    elif(y > x):
        ch = ch + "counting up "
        for i in range(x,y+1):
            ch = ch + str(x) + " "
            x = x + 1
    return(ch)


print(counter(1,10))
print(counter(10,1))