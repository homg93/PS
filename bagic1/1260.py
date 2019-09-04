from sys import stdin

n,m,v = map(int, input().split())
a = [[] for i in range(n+1)]
for i in range(m):
	d1,d2 = map(int, input().split())
	a[d1].append(d2)
	a[d2].append(d1)
for i in range(1,n+1):
	a[i] = sorted(a[i])
check = [0 for i in range(n+1)]
def bfs(v):
	check = [0 for i in range(n+1)]
	q = []
	check[v] = True
	q.append(v)
	while(len(q)):
		x = q[0]
		print(q.pop(0),end=' ')
		for i in range(len(a[x])):
			if (check[a[x][i]] == 0):
				check[a[x][i]] = True
				q.append(a[x][i])

def dfs(x):
	check[x] = True
	print(x,end=' ')
	for y in a[x]:
		if check[y] == 0:
			dfs(y)

dfs(v)
print()
bfs(v)
print()