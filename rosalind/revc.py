
import utils

def translate(dna):
    rna = ""
    complecements = {
        'A':'T',
        'T':'A',
        'C':'G',
        'G':'C'
    }

    for i in range(1, len(dna)+1):
        rna+=complecements[dna[-i]]
    return rna

print(translate("AAAACCCGGT"))

print(translate(utils.read_file("rosalind_revc.txt")))