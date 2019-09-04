n,k = map(int,input().split())
check = [0 for _ in range(100001)]
dist = [0 for _ in range(100001)]
def bfs(x):
	q = []
	check[x] = 1
	q.append(x)

	while len(q):
		if check[k] == 1:
			break
		x = q.pop(0)
		for i in range(3):
			if i == 0:
				nx = x-1
			elif i == 1:
				nx = x+1
			elif i == 2:
				nx = x+x
			if 0<= nx <=100000:
				if check[nx] == 0:
					dist[nx] = dist[x] + 1
					check[nx] = 1
					q.append(nx)
dist[n] = 1
bfs(n)
print(dist[k]-1)
