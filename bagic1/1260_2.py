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
	q = []
	check[v] = True
	q.append(v)

	while len(q):
		x = q.pop(0)
		print(x,end=' ')
		for y in a[x]:
			if check[y] == 0:
				check[y] = True
				q.append(y)
bfs(v)
print()
