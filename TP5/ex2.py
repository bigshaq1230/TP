dict = {"Ali": 15, "Mariem": 16, "Mohamed": 12, "Fatma": 13, "Yessine": 18}

for i in dict:
    print(i+" ",end="")
print()


for i in dict:
    if(i == "Mohamed"):
        dict[i] = 14

print(dict)
avg = sum(dict.values()) / len(dict)
print("average: ",avg)

max = max(dict.values())
for i in dict:
    if(dict[i] == max):
        print("the best: ",i)

input = int(input("write a grade: "))
def lower_notes(k,dict):
    for i in dict:
        if(dict[i] < k):
            print(i," ",end="")
    print()


lower_notes(input,dict)