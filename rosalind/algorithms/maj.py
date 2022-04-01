def readMajorityElementFile(fname):
    f = open(fname, 'r')
    kn = f.readline().strip().split(" ")
    k = int(kn[0])
    n = int(kn[1])
    arrs = []
    for i in range(k):
        arrs.append(list(map(lambda x : int(x), f.readline().strip().split(" "))))
    return k,n, arrs

def findAllMajorityElements(k,n,arrs):
    majors = []
    for i in range(k):
        majors.append(str(findMajorityElement(n,arrs[i])))
    return " ".join(majors)
def findMajorityElement(n,arr):
    half = n//2+1
    dic = {}
    j=0
    for elem in arr:
        if elem in dic:
            dic[elem]+=1
            if dic[elem]>=half:
                return str(elem)
        else:
            dic[elem]=1
        j+=1
    return "-1"

if __name__ == '__main__':
    k,n,arrs = readMajorityElementFile("rosalind_maj.txt")
    print(findAllMajorityElements(k,n,arrs))
    #print(findAllMajorityElements(k,n,arrs))
