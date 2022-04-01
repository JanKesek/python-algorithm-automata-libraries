from utils import parseFASTA

def findOverlapGraph(dic):
    graph = {}
    for j in dic:
        for k in dic:
            if doesDNAsOverlap(j,k,dic,graph):
                graph[(j,k)]=None
    return list(dict.fromkeys(graph))
def findOverlapGraphParseToOutput(dic, outputFname):
    graph = findOverlapGraph(dic)
    s = ""
    for g in graph:
        l = ""
        for gg in g:
            l += gg.replace(">","").strip()+" "
        s+= l.strip()
        s+="\n"
    s = s.strip()
    with open(outputFname, 'w') as f:
        f.write(s)
def doesDNAsOverlap(jkey, kkey, dic, graph):
    if jkey != kkey and (jkey, kkey) not in graph:
        jDNA = dic[jkey]
        kDNA = dic[kkey]
        return hasSamePrefix(jDNA, kDNA,3)
    return False
def hasSamePrefix(jDNA, kDNA,k):
    if jDNA == kDNA:
        return False
    jSuffix = ""
    kPrefix = ""
    #print("{} {}".format(jDNA, kDNA)) 
    i=0
    j=1
    while i< len(kDNA) and j<= len(jDNA):
        jSuffix += jDNA[-j]
        kPrefix += kDNA[i]
        i+=1
        j+=1
        if len(kPrefix) >=k and len(jSuffix) >=k:
            if kPrefix == jSuffix:
                return True
            return False
    return False
if __name__=='__main__':
    print(findOverlapGraphParseToOutput(parseFASTA("rosalind_grph_test.txt"), "rosalind_graph_output_test.txt"))
    #print(findOverlapGraphParseToOutput(parseFASTA("rosalind_grph_test2.txt"), "rosalind_graph_output_test.txt"))
    print(findOverlapGraphParseToOutput(parseFASTA("rosalind_grph.txt"), "rosalind_graph_output.txt"))