def saveToFile(s, fname):
    with open(fname, 'w') as f:
        f.write(s)
def twoLinesImport(fname):
    f = open(fname, 'r')
    n = f.readline().strip()
    narr = list(map(lambda x : int(x), f.readline().strip().split(" ")))
    return int(n), narr
def readGraphEdgeList(fname):
    f = open(fname, 'r')
    nm = f.readline().strip().split(" ")
    n=int(nm[0])
    m=int(nm[1])
    edges = []
    for i in range(m):
        edges.append(list(map(lambda x : int(x), f.readline().strip().split(" "))))
    return n,m,edges
def createGraphDic(edgeList):
    graph ={}
    for e in edgeList:
        if e[0] not in graph:
            graph[e[0]] = set()
        if e[1] not in graph:
            graph[e[1]] = set()
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph
def createGraphDicDirected(edgeList):
    graph ={}
    for e in edgeList:
        if e[0] not in graph:
            graph[e[0]] = set()
        graph[e[0]].add(e[1])
    return graph

