import itertools

def findPerms(n):
    lst = [i for i in range(1,n+1)]
    perms = list(itertools.permutations(lst))
    print(len(perms))
    s = ""
    for p in perms:
        for pp in p:
            s+=str(pp) + " "
        s+="\n"
    print(s)
def findSignedPermutations(n):
    lst = [i for i in range(1,n+1)]
    s = ""
    signedPermLength = 0
    for p in itertools.permutations(lst):
        for signs in itertools.product([-1,1],repeat=n):
            for pp in [a*sign for a,sign in zip(p,signs)]:
                s+=str(pp) + " "
            s+="\n"
            signedPermLength += 1
    print(signedPermLength)
    print(s)
#findPerms(3)
#findPerms(5)

#findSignedPermutations(2)
findSignedPermutations(3)