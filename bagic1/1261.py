from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y):
	q = deque()
	q.append((x,y))
	dist[x][y] = 0
	while len(q):
		x,y = q.popleft()
		for k in range(4):
			nx,ny = x + dx[k], y + dy[k]
			if 0<=nx<h and 0<=ny<w:
				if dist[nx][ny] == -1:
					if a[nx][ny] == 0:
						dist[nx][ny] = dist[x][y]
						q.appendleft((nx,ny))
					else:
						dist[nx][ny] = dist[x][y]+1
						q.append((nx,ny))
				

w,h = map(int,input().split())
a = [list(map(int,list(input()))) for _ in range(h)]
dist = [[-1]*w for _ in range(h)]
			
bfs(0,0)
print(dist[h-1][w-1])