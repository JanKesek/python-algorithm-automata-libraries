from grph import hasSamePrefix
from utils import parseFASTA

def testOverlapGraphs():
    lines = []
    dic = parseFASTA("rosalind_grph.txt")
    print(list(dic))
    with open('rosalind_graph_output.txt','r') as f:
        lines2 = f.readlines()
        for l in lines2:
            jk = l.strip().split(" ")
            if not hasSamePrefix(dic[jk[0]], dic[jk[1]],3):
                print("FOUND ERROR {} {} ".format(jk))
testOverlapGraphs()
    