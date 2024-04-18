p = [[0.5,0.3,0.2],[0.2,0.8,0],[0.3,0.3,0.4]]
g = [[0,0,0],[0,0,0],[0,0,0]]
def isStochastcic(p):
    state = True
    i = 0
    while(state and i<len(p)):
        sum = 0
        for j in range(len(p)):
            sum = sum + p[i][j]
        i = i + 1
        if(sum != 1):
            state = False
    return state


def isBistoctic(p):
    if(isStochastcic(p) == False):
        return False
    j = 0
    while(j<len(p)):
        sum = 0
        for i in range(len(p)):
            sum = sum + p[i][j]
        j = j + 1
        if(sum != 1):
            return False
    return True

def multply_vec(p,g):
    t = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(p)):
        for j in range(len(g)):
            sum = 0
            for i2 in range(len(p)):
                sum = sum + (p[i][i2] * g[i2][j])
            t[i][j] = sum
    return t




def stable_vec(p,g):
    l = len(p)
    p = p
    g = g
    t = multply_vec(p,g)
    for i in range(l):
        for j in range(l):
            if (t[i][j] != g[i][j]):
                return False

    return True


print(isStochastcic(p))
print(isBistoctic(p))
print(stable_vec(p,g))