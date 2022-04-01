import utils

def calculateGCContent(dna):
    counter = 0
    for c in dna:
        if c=='G' or c=='C':
            counter +=1
    m = len(dna.strip())
    #print( "{} : {}  : {} == {}".format(dna,counter,m, counter / m) )
    return counter / m
def findContentForEachString(dnadic):
    percentdic ={}
    for id in dnadic:
        percentdic[id] = calculateGCContent(dnadic[id])
    return percentdic
def findHighestGCContent(dnadic):
    #print(dnadic)
    percentdic = findContentForEachString(dnadic)
    #print(percentdic)
    d =  max(percentdic, key=percentdic.get)
    return d + "\n" + str(percentdic[d] * 100)
dnas = utils.parseFASTA("sample_fasta.txt")
dnas2 = utils.parseFASTA("rosalind_gc.txt")
#print(dnas2)
print(findHighestGCContent(dnas))
calculateGCContent("AGCTATAG")
print(findHighestGCContent(dnas2))

