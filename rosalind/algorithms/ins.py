from utils import twoLinesImport


def insertionSort(n, arr):
    swapCounter = 0
    for i in range(1,n):
        k=i
        while k>0 and arr[k]<arr[k-1]:
            arr =swap(k-1,k,arr)
            k=k-1
            swapCounter+=1
    return arr, swapCounter
def swap(i,j,arr):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return arr
if __name__ =='__main__':
    n, arr = twoLinesImport("rosalind_ins.txt")
    print(insertionSort(n,arr))