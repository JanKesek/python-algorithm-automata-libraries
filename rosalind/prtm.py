from utils import createMonosoicMassTable, read_file
def calculateProteinMass(s):
    dic = createMonosoicMassTable()
    m=0
    for c in s.strip():
        m+= dic[c]
    return round(m,3)

print(calculateProteinMass("SKADYEK"))
print(calculateProteinMass(read_file("rosalind_prtm.txt")))