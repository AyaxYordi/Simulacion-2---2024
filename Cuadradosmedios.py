from math import *

def mid(n,s):
	if n==0:
		return s
	if n>0:
		return ((mid(n-1,s)**2)//100)%10000

def periodo(seed):
	l = []

	for i in range(10):
		l.append(mid(i,seed))
		
	return len(set(l))

#for i in range(1000,9999):
#	print(i,periodo(i))


#for j in range(60):
#	print(mid(j,9990))


for j in range(1000,9999):
	if periodo(j)==2:
		print(j)
		
		
