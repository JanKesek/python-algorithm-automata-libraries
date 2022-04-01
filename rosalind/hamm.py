import imp


import utils

def hamming(s, t):
    h=0
    for i in range(len(s)):
        if s[i] != t[i]:
            h+=1
    return h

print(hamming("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))
hamms = utils.read_2_line_input("hamming.txt")
print(hamms)
print(hamming(hamms[0].strip(),hamms[1].strip()))
