n = int(input("give n: "))

while(n<0 or n>9999):
    n = int(input("give n: "))

i = 1
sum = 0
while(i <= n//2):
    if(n%i==0):
        sum = sum + i
    i = i + 1


if(sum == n):
    print("perfect number")