
def countPairs(n,k):
    pairs =[-1]
    smalls = 1
    bigs = 0
    for i in range(n):
        newpairs=[]
        for j in range(len(pairs)):
            if pairs[j] == -1:
                pairs[j]=1
            else:
                for l in range(k):
                    newpairs.append(-1)
        pairs.extend(newpairs)
        print(pairs)
    return len(newpairs)-2
def countPairs2(n,k):
    rabits = [ -1 ]
    lens=[]
    lastone = 1
    for i in range(1,n):
        newrabbits = []
        for r in rabits:
            if r==-1:
                newrabbits.append(1)
            else:
                newrabbits.append(1)
                for j in range(k):
                    newrabbits.append(-1)
        rabits = newrabbits
        lastone = len(newrabbits)
        print(rabits)
    return lastone
def countPairs3(n,k):
    little = 1
    bigs = 0
    for i in range(1,n):
        littletemp = little
        bigs += little
        little = 0
        little += (bigs-littletemp)*k
        print(bigs+little)
    return bigs+little
def countPairsDying(n,m):
    little = 1
    bigs = 0
    for i in range(1,n):
        littletemp = little
        bigs += little
        little = 0
        little += (bigs-littletemp)*k
        print(bigs+little)
    return bigs+little
def fib(n,k):
    f = [k,1]
    for i in range(0,n):
        f.append(f[-1]+f[-2])
    return f
print(countPairs3(5,3))
#print(fib(5,3))

print(countPairs3(32,5))