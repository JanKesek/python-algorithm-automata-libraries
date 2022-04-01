with open('rosalind_dna.txt','r') as f:
    text = f.read()
def tranmsalte(text):
    ac=0
    cc= 0
    gc=0
    tc=0
    for c in text:
        if 'A'==c:
            ac+=1
        if 'C'==c:
            cc+=1
        if 'G' ==c:
            gc+=1
        if c=='T':
            tc+=1
    return ac,cc,gc,tc
act,cct,gct,tct = tranmsalte("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
ac,cc,gc,tc = tranmsalte(text)
print("{} {} {} {}".format(act,cct,gct,tct))
print("{} {} {} {}".format(ac,cc,gc,tc))