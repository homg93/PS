from collections import deque
dy = [1,-1,0,0]
dx = [0,0,1,-1]
def bfs(x,y,z):
	q = deque()
	q.append((x,y,z))
	dist[x][y][z] = 1
	while len(q):
		x,y,z = q.popleft()
		for k in range(4):
			nx,ny = x + dx[k], y + dy[k]
			if 0<=nx<h and 0<=ny<w:
				if dist[nx][ny][z] == 0 and a[nx][ny] == 0:
					dist[nx][ny][z] = dist[x][y][z]+1
					q.append((nx,ny,z))
				if z == 0 and dist[nx][ny][z+1] == 0 and a[nx][ny] == 1:
					dist[nx][ny][z+1] = dist[x][y][z]+1
					q.append((nx,ny,z+1))
				

h,w = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(h)]
# dist = [[-1]*w for _ in range(h)]
dist = [[[0]*2 for j in range(w)] for i in range(h)]

bfs(0,0,0)
if dist[h-1][w-1][0] != 0 and dist[h-1][w-1][1] !=0:
	print(min(dist[h-1][w-1][0],dist[h-1][w-1][1]))
elif dist[h-1][w-1][0] == 0 and dist[h-1][w-1][1] ==0:
	print(-1)
else:
	print(max(dist[h-1][w-1][0],dist[h-1][w-1][1]))
