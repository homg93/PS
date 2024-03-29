import sys
sys.setrecursionlimit(1000000)

def dfs(x,c):
	check[x] = c
	for y in a[x]:
		if check[y] == 0:
			if dfs(y,3-c) == 0:
				return 0
		elif check[y] == check[x]:
			return 0
	return 1


k = int(sys.stdin.readline())
for i in range(k):
	n,m = map(int, sys.stdin.readline().split())
	a = [[] for i in range(n+1)]
	check = [0 for i in range(n+1)]
	c = 1
	ok = 1

	for i in range(m):
		d1,d2 = map(int, sys.stdin.readline().split())
		a[d1].append(d2)
		a[d2].append(d1)

	for i in range(n):
		if check[i] == 0:
			if not dfs(i,1):
				ok = False
				break
	print("YES" if ok else "NO")
