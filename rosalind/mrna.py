import utils

def findNumberOfPossibleRNAStrings(protein):
    codonDic = utils.createCodonDic()
    lst = []
    k=0
    for ch in protein:
        
        for codon in codonDic:
            if codonDic[codon] == ch:
