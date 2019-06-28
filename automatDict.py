
DFA = {}

def convert(NFA):
	for key,value in NFA.items():
		#print(value)
		for przejscia in value:
			#print("COT O KURWA JEST", przejscia[1])
			if len(przejscia[1])>1:
				newKey=[''.join(przejscia[1])]
				#flatList= [item for sublist in DFA.values() for item in sublist]
				if newKey not in DFA.values():
					t=[]
					w=[]
					w.append(przejscia[0])
					w.append(newKey)
					t.append(w)
					#print("JAPIERDOLE", t)
					DFA[key]=t
			else:
				#flatList= [item for sublist in DFA.values() for item in sublist]
				if przejscia[1] not in DFA.values():
					t=[]
					w=[]
					w.append(przejscia[0])
					w.append(przejscia[1])
					t.append(w)
					#print("NIEW KURWIAJ MNIE", w)
					DFA[key]=w
		print(DFA)
		print(NFA)
		for keys, values in DFA.items():
			for przejscia in values:
				for nodes in przejscia[1]:
					if len(nodes)>1:
						for letters in nodes:
							for trs in NFA[letters]:
								for newStates in trs[1]:
									if type(newStates)!=list: break
									for state in newStates:
										if state not in DFA.keys():
											t=[NFA[letters][0], state]
											DFA[nodes]=[]
											DFA[nodes].append(t)
NFA= {'A': [[1,['B','C']]],'B': [[1,['B','C']],[0,['B']]]}
convert(NFA)
print(DFA)