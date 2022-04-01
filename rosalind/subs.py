from utils import read_file, read_2_line_input

def findLocationsOfSubstring(s, subS):
    i = 0
    k = len(subS)
    sLength = len(s) 
    locations = []
    while i< sLength - k:
        if s[i:i+k] == subS:
            locations.append(i+1)
        i+=1
    return locations
def findLocationsOfSubstringParse(s, subS):
    lst = findLocationsOfSubstring(s, subS)
    lstStrings = [str(k) for k in lst]
    return " ".join(lstStrings)
inp= read_2_line_input("rosalind_subs.txt")
print(findLocationsOfSubstringParse("GATATATGCATATACTT", "ATAT"))
print(findLocationsOfSubstringParse(inp[0],inp[1]))