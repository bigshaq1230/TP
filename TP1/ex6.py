t = []

n = int(input("give n: "))

def is_prime(x):
    for i in range(2,x//2):
        if(x%i ==0):
            return False
    return True


for i in range(2,100):
    if(is_prime(i)):
        t.append(i)


print("primes to 100: ",t)

l = len(t)
def func(n):
    for i in range(l-1):
        for j in range(i):
            if (t[i] + t[j] == n):
                print(n," = ",t[i],"+",t[j])
                return

func(n)

