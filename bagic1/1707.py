from sys import stdin
import sys
sys.setrecursionlimit(1000000)
def dfs(x,c):
	check[x] = c
	# print(x,end=' ')
	for y in a[x]:
		if check[y] == 0:
			if not dfs(y,3-c):
				return False
		elif check[y] == check[x]:
			return False
	return True



k = int(stdin.readline())
for i in range(k):
	n,m = map(int, stdin.readline().split())
	a = [[] for i in range(n+1)]
	check = [0 for i in range(n+1)]
	c = 1

	for i in range(m):
		d1,d2 = map(int, stdin.readline().split())
		a[d1].append(d2)
		a[d2].append(d1)

	ok = True
	# for i in range(1,n+1):
	# 	for y in a[i]:
	# 		if check[i] == check[y]:
	# 			ok = False
	for i in range(n):
		if check[i] == 0:
			if not dfs(i,1):
				ok = False
				break
	print("YES" if ok else "NO")
