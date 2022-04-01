from utilsAlgo import readGraphEdgeList

def calculateGraphDegrees(edgeList,n):
    graph ={}
    for e in edgeList:
        if e[0] not in graph:
            graph[e[0]] = set()
        if e[1] not in graph:
            graph[e[1]] = set()
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    output = ""
    for i in range(1,n+1):
        output += str(len(graph[i])) + " "
    return output
def calculateGraphDoubleDegrees(edgeList,n):
    graph ={}
    for e in edgeList:
        if e[0] not in graph:
            graph[e[0]] = set()
        if e[1] not in graph:
            graph[e[1]] = set()
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    output = ""
    for i in range(1,n+1):
        counter = 0
        if i in graph:
            neighbours = list(graph[i])
            for n in neighbours:
                counter += len(graph[n])
        output += str(counter) + " "
    return output
    
if __name__ == '__main__':
    #n,m,arr = readGraphEdgeList("rosalind_deg.txt")
    #print(calculateGraphDegrees(arr,n))
    n,m,arr = readGraphEdgeList("rosalind_ddeg.txt")
    print(arr)
    print(calculateGraphDoubleDegrees(arr,n))