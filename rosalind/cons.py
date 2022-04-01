from utils import parseFASTA, saveToFile

def createProfileMatrix(dnas, dnaLength):
    profile = {
        a: [0 for i in range(dnaLength)] for a in ['A','C','G','T']
    }
    for dna in dnas:
        for i in range(len(dna)):
            profile[dna[i]][i]+=1
    return profile
def createConsensusAndProfileParse(dic):
    dnas = list(dic.values())
    dnaLength = len(dnas[0])
    profile = createProfileMatrix(dnas, dnaLength)
    consensus = ""
    for i in range(dnaLength):
        m=-1
        maxD = 'A'
        for d in profile.keys():
            if profile[d][i] >= m:
                m=profile[d][i]
                maxD=d
        consensus += maxD
    s = consensus + "\n"
    for d in profile:
        s+= "{}: ".format(d) 
        lst = [str(ss) for ss in profile[d]]
        s += " ".join(lst) +"\n"
    return s

dic = parseFASTA("rosalind_cons_test.txt")
dic2 = parseFASTA("rosalind_cons.txt")
#print(createConsensusAndProfileParse(dic))
saveToFile(createConsensusAndProfileParse(dic2), "rosalind_cons_output.txt")