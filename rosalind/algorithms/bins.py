from utils import saveToFile

def readBinarySearchFile(fname):
    f = open(fname, 'r')
    n = f.readline().strip()
    m = f.readline().strip()
    narr = list(map(lambda x : int(x), f.readline().strip().split(" ")))
    marr = list(map(lambda x : int(x), f.readline().strip().split(" ")))
    #marr = f.readline().strip().split(" ")
    return n,m,narr,marr

def binarySearch(beg, end, piv, arr, elem):
    if beg >= end:
        return -1
    curr = arr[piv]
    if curr == elem:
        return piv+1
    elif curr > elem:
        return binarySearch(beg, piv, (beg+piv)//2,arr,elem)
    else:
        return binarySearch(piv+1, end, (piv+end)//2, arr, elem)
def findAllIndicesOfMInN(nS,narr,marr):
    indices = []
    n = int(nS)
    for elem in marr:
        indices.append(str(binarySearch(0,n,n//2,narr,elem)))
    return " ".join(indices)
n,m,narr,marr = readBinarySearchFile("rosalind_bins.txt")
#print(n)
#print(m)
#print(narr)
#print(marr)

saveToFile(findAllIndicesOfMInN(n,narr,marr), "rosalind_bins_output.txt")