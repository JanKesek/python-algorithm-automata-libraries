from xmlrpc.client import MAXINT
from utilsAlgo import readGraphEdgeList, createGraphDicDirected, saveToFile

def findAllShortestPaths(graph,n):
    paths = []
    dic = bfs2(graph, 1,n)
    nodes = [i for i in range(1, n+1)]
    for elem in nodes:
        if dic[elem]==MAXINT:
            paths.append("-1")
        else:
            paths.append(str(dic[elem]))
    return " ".join(paths)
def bfs3(edgeList, start, n):
    dist ={}
    for i in range(1,n+1):
        dist[i] = -1
    dist[start]=0
    q = [start]
    while len(q) != 0:
        u = q.pop()
        for edge in edgeList:
            if dist[edge[1]] == -1:
                q.append(edge[1])
                dist[edge[1]]=dist[edge[0]]+1
    return dist
def bfs2(graph, s,n):
    #print("GRAPH {}".format(graph))
    dist = {s: 0}
    if s in graph:
        for i in range(1,n+1):
            dist[i]=MAXINT
        dist[s]=0
        q = [s]
        while len(q) != 0:
            u = q.pop()
            if u in graph:
                for v in graph[u]:
                    if dist[v] == MAXINT:
                        q.append(v)
                        dist[v]=dist[u]+1
    return dist
def bfs(graph, source, target, visited, pathLength = 0, debug = False):
    visited[source]=True
    if debug:
        print("{} {} {}".format(graph, source, target))
    if source == target:
        return pathLength
    for neighbour in graph[source]:
        if visited[neighbour] == False and neighbour in graph:
            if debug:
                print("{} {} {} NEIGHBOR {} VISITED {} {}".format(graph, source, target, neighbour, visited, visited[neighbour]))
            return bfs(graph,neighbour, target,visited,pathLength+1, debug=debug)
    return -1
def test(fname, debug = False):
    n,m,edgeList = readGraphEdgeList(fname)
    #print(bfs3(edgeList,1,n))
    graph = createGraphDicDirected(edgeList)
    if debug:
        print(findAllShortestPaths(graph,n))
    else:    
        saveToFile(findAllShortestPaths(graph,n), "rosalind_bfs_output.txt")
if __name__ =='__main__':
    test("rosalind_bfs_test.txt",True)
    test("rosalind_bfs.txt",True)