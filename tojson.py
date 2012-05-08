
def _tojson(a,b,sarr):
	sa = len(a)
	sb = len(b)
	if (sa < sb):
		for f in sa:
			sarr.append('"f":[')
	elif (sa > sb):
		

def tojson(lines,c='/'):
	arr = []
	for i in range(1,len(lines)):
		a = lines[i-1].split(c)
		b = lines[i].split(c)
	

import sys
import platform

lines = sys.stdin.readlines()

tojson([line for line in lines])
