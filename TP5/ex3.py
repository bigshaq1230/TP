def revesee(list):
    list.reverse()

def reduce(list,k):
    l2 = []
    for i in list:
        if(i == k):
            continue
        l2.append(i)
    return l2

def func(list,k=None):
    if k is not None:
        list = reduce(list,k)
    revesee(list)
    return (list)

l = [1,2,3,4]

print(func(l,1))
print(func(l))