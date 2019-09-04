from sys import stdin

n ,m = map(int, stdin.readline().split())
a = [0 for i in range(n+1)]
c = [0 for i in range(n+1)]
def go(index,n,m):
	if index == m:
		for num in a:
			if num != 0:
				print(num, end=' ')
		print()
		return

	for i in range(1,n+1):
		print("index=%d, i=%d"%(index,i))

		if c[i]:
			continue
		c[i] = 1
		a[index] = i
		go(index+1,n,m)
		c[i] = 0
go(0,n,m)
