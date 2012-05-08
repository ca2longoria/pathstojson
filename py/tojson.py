
def _tojson(a,b,sarr):
	sa = len(a)
	sb = len(b)
	if (sa < sb):
		for i in range(sb-sa-1):
			ind = len(a)-1-(sb-sa)+i
			sarr.append('"'+str(a[ind])+'":[')
	elif (sa > sb):
		for i in range(sa-sb):
			ind = len(b)-1-(sa-sb)+i
			sarr.append('], ')
	return sarr

def tojson(lines,c='/'):
	arr = []
	for i in range(1,len(lines)):
		a = lines[i-1].split(c)
		b = lines[i].split(c)
		_tojson(a,b,arr)
	print ''.join(arr[:])

import sys
import platform

lines = sys.stdin.readlines()

tojson([line for line in lines])
