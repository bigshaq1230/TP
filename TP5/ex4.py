ensb = {13,10,2,1,5,8,13}
print(ensb)
print("we observe that the set is printed in a sorted order")

x = int(input("give a number: "))
ensb.add(x)
print(ensb)

print("exmaple of adding a value that does not exist in the set: ",100)
ensb.add(100)
print(ensb)

print("exmaple of adding a value that does exist in the set: ",13)
ensb.add(13)
print(ensb)
print("the value is not added because it exist in the set")


if ensb:
    popped_element = ensb.pop()
    print("Popped element:", popped_element)
    print("Set after popping:", ensb)
else:
    print("The set is empty.")


def empty(g):
    if (g):
        print("set not empty")
        return False
    else:
        print("set empty")
        return True
m = {}
print(m)
empty(m)
print(ensb)
empty(ensb)
