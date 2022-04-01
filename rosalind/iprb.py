from ntpath import join


def dominantAlleleProbability(homozygD, heterozyg,homozygR):
    s = homozygR + homozygD + heterozyg
    aAaA = jointProbability(heterozyg, heterozyg, s,True) * 0.25
    aaAa = jointProbability(homozygD,heterozyg,s,False) * 0.5
    aaaa = jointProbability(homozygD, homozygD,s,True) 
    return aAaA + aaAa + aaaa

def jointProbability(e1,e2, s, sameEvent=False):
    if sameEvent:
        return ((e1)/s)*((e2-1)/(s-1))
    else:
        return ((e1)/s)*((e2)/(s-1))
print(dominantAlleleProbability(2,2,2))