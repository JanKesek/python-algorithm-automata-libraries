#RNA: convert all T into U
import utils

def translate(dna):
    rna = ""
    for d in dna:
        if d=='T':
            rna += 'U'
        else:
            rna += d
    return rna

print(translate("GATGGAACTTGACTACGTAAATT"))
print(translate(utils.read_file("rosalind_rna.txt")))
#GAUGGAACUUGACUACGUAAAUU
#GAUGGAACUUGACUACGUAAAUU