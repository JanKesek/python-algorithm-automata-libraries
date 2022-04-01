import re
import utils


def parseRNAToProtein(rna):
    codonDic = utils.createCodonDic()
    k=3
    protein = ""
    while k<=len(rna):
        codon = rna[k-3:k]
        code = codonDic[codon]
        if code != "Stop":
            protein += code.strip()
        k+=3
    return protein
rnalong = utils.read_file("rosalind_prot.txt")
print(parseRNAToProtein("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"))

print("PRZERWA")
print(parseRNAToProtein(rnalong))
