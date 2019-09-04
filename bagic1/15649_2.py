from sys import stdin

def go(parr, i,check):
	if i == m:
		for c in parr:
			print(c,end=' ')
		print()
		return
	if i > m:
		return
	for k in range(n):
		if not check[k]:
			check[k] = 1
			go(parr+str(a[k]),i+1,check)
			check[k] = 0


n,m = map(int,stdin.readline().split())
a = [i for i in range(1,n+1)]
check = [0 for i in range(n)]
go("",0,check)