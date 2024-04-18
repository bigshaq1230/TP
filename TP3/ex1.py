l = [10,18,14,20,12,16]
def minmaxavg(l):
    min = l[0]
    max = l[0]
    avg = 0
    for i in range(len(l)):
        avg = avg + l[i]
        if(min>l[i]):
            min = l[i]
        if(max<l[i]):
            max = l[i]

    
    newavg = l[0]
    avg = avg/len(l)+1
    for i in range(len(l)):
        if abs(l[i]-avg) < abs(l[i]-newavg):
            newavg = l[i]




    return(min,max,newavg)



print(minmaxavg(l))