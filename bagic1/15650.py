from sys import stdin

def go(index,start):
	print("index,start=%d,%d"%(index,start))
	if index == m:
		for c in a:
			if c != 0:
				print(c,end=' ')
		print()
		return
	for i in range(start,n+1):
		a[index] = i
		go(index+1,i+1)


n,m = map(int,stdin.readline().split())
a = [0 for i in range(n)]
go(0,1)