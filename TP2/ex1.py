def betterprint(my_dict):
        for key, value in my_dict.items():
            print(f" {key}: {value}  ",end="")
        print()

cars = [
    {"brand": "Volkswagen", "model": "Golf", "plate_number": "102TN155", "color": "red", "power": 7},
    {"brand": "Renault", "model": "Clio", "plate_number": "506TN201", "color": "black", "power": 4},
    {"brand": "Peugeot", "model": "407", "plate_number": "8002TN", "color": "white", "power": 6},
    {"brand": "Volkswagen", "model": "Polo", "plate_number": "4000TN122", "color": "gray", "power": 5}
]

for i in range(len(cars)):
    if(cars[i]["power"]>= 5):
        betterprint(cars[i])

brand = input("give brand name: ")

exist = False

for i in cars:
    if (i["brand"] == brand):
        betterprint(i)
        exist = True
if (exist == False):
    print("n'existe pas")


for i in cars:
    if(i["color"] == "red"):
        i["color"] = "green"
for i in cars:
    betterprint(i)
