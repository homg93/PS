from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y):
	# cant = 0
	cnt = 1
	q = deque()
	q.append((x,y))
	check[x][y] = True
	while q:
		x,y = q.popleft()
		cnt+=1
		for k in range(4):
			nx, ny = x+dx[k], y+dy[k]
			if 0<=nx<n and 0<=ny<m:
				if a[nx][ny] == 1 and check[nx][ny] == 0:
					q.append((nx,ny))
					dist[nx][ny] = dist[x][y] +1
					check[nx][ny] = check[x][y] +1

n,m = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(n)]
check = [[0]*m for _ in range(n)]
dist = [[0]*m for _ in range(n)]
dist[0][0] = 1
bfs(0,0)
print(dist[n-1][m-1])

for cc in check:
	print(cc)
