import itertools
alphabet=['0','1']
def powerset(lst):
	lst1=[]
	for i in range(0,len(lst)+1):
		lst2=[list(x) for x in itertools.combinations(lst,i)]
		lst1.extend(lst2)
	return lst1
DFA={}
def constructDFA(NFA, subsets, alphabet):
	for lst in subsets:
		DFA[str(lst)]={}
		for c in alphabet:
			t=[]
			for s in lst:
				if s in NFA.keys():
					if NFA[s] is not None:
						if c in NFA[s].keys():
							t.extend(NFA[s][c])
			#print(lst)
			#print(c)
			#print(t)
			DFA[str(lst)][c]=str(t)
def minimizeTable(dfa, startState,finishState, visited):
	if startState in finishState: return visited
	for key, val in dfa[startState].items():
		if val not in visited:
			print(val)
			visited.append(val)
			minimizeTable(dfa,str(val), finishState, visited)
def minimize(dfa, necessaryStates):
	minDFA={}
	for s in necessaryStates:
		minDFA[str(s)]=dfa[str(s)]
	return minDFA
def isMatch(string, dfa,startState,finishState):
	if len(string)==1: 
		return dfa[startState][string[0]] in finishState
	else:
		return isMatch(string[1:], dfa, dfa[startState][string[0]],finishState)
NFA = {1: {'0':[1,2], '1':[1]}, 2: { '1':[3]}, 3: None}
#NFA2= {1:{'a':[1,2],'b':[1]},2: {'a':[3],'b':[3]},3:None}
subsets = powerset(NFA.keys())
subsets=subsets[1:]
print(subsets)
constructDFA(NFA,subsets, alphabet)
print(DFA)
v=[]
startState='[1]'
finishState=[]
for keys,value in DFA.items():
	if '3' in keys: finishState.append(keys)
#print(finishState)
minimizeTable(DFA, startState,finishState,v)
print(v)
minDFA=minimize(DFA,v)
print(minDFA)
print(isMatch('1111101111111100100000',minDFA,startState,finishState))

