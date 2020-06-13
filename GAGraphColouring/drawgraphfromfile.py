import re
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib
import random

def parseMatrix(m):
    adjM=[]
    lines=m.split("\n")
    for l in lines:
        row=[]
        for c in l:
            if c.isnumeric(): row.append(int(c))
        if len(row)!=0: adjM.append(row)
    assert(len(adjM)==len(adjM[0]))
    #assert(len(adjM[0])==20)
    return adjM
def parseColours(colours):
    numbers=re.findall(r'\[([0-9])\]',colours)
    return [int(n) for n in numbers]
def drawGraph(adjM,colours):
    adjM=np.array(adjM)
    colour_map=makeColourMap(colours)
    G=nx.from_numpy_matrix(adjM)
    nx.draw(G,node_color=colour_map)
    plt.show()
def makeColourMap(colours):
    #possiblecolours=[list(matplotlib.colors.cnames.keys())]
    possiblecolours=['black', 'blanchedalmond', 'blue', 'blueviolet']
    print(possiblecolours)
    #colourMap={ i:possiblecolours[random.randint(0,len(possiblecolours)-1)] for i in range(0,4) }
    colourMap={i:possiblecolours[i] for i in range(len(possiblecolours))}
    return [colourMap[n] for n in colours]
with open('graph_file.txt','r') as f:
    text=f.read()

adjacencyM=text.split("<==>")[0]
colours=text.split("<==>")[1]

adjacencyM=parseMatrix(adjacencyM)
colours=parseColours(colours)
print(adjacencyM)
print(colours)
drawGraph(adjacencyM, colours)