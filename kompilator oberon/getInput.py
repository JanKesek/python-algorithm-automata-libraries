import sys
import re
t=[]
ident=0
lparen=3
lbrak=4
lbrace=5
bar=6
eql=7
rparen=8
rbrak=9
rbrace=10
period=11
other=12
#for line in sys.stdin:
	#t.append(list(line))

for lines in sys.stdin:
	for c in list(lines):
		if re.match('[a-zA-Z]',c):
			sym=ident
			i=0
		elif c=='=': sym=eql
		elif c=='(': sym=lparen
		elif c==')': sym=rparen
		elif c=='[': sym=lbrak
		elif c==']': sym=rbrak
		elif c=='{': sym=lbrace
		elif c=='}': sym=rbrace
		elif c=='|': sym=bar
		elif c=='.': sym=period
		else: sym=other
		print(sym)
print(sys)