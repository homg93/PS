from collections import deque
n,k = map(int,input().split())
dist = [-1 for _ in range(100001)]
def bfs(x):
	q = deque()
	dist[x] = 0
	q.append(x)

	while len(q):
		if dist[k] != -1:
			break
		x = q.popleft()
		for i in range(3):
			if i == 0:
				nx = x+x
			elif i == 1:
				nx = x+1
			elif i == 2:
				nx = x-1
			if 0<= nx <=100000:
				if dist[nx] == -1:
					if i ==0:
						dist[nx] = dist[x]
						q.appendleft(nx)
					else:
						dist[nx] = dist[x] + 1
						q.append(nx)
bfs(n)
print(dist[k])
