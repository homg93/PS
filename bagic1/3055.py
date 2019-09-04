from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
r, c = map(int,(input().split()))
a = [list(input()) for _ in range(r)]
check = [[-1]*c for _ in range(r)]
dist = [[-1]*c for _ in range(r)]
q = deque()
for i in range(r):
	for j in range(c):
		if a[i][j] == '*':
			check[i][j] = 0
			q.append((i,j))
		elif a[i][j] == 'S':
			sx,sy = i,j
		elif a[i][j] == 'D':
			end_x, end_y = i,j
while q:
	x,y = q.popleft()
	for k in range(4):
		nx, ny = x + dx[k], y + dy[k]
		if 0<=nx<r and 0<=ny<c:
			if a[nx][ny] in 'XD':
				continue
			if check[nx][ny] != -1:
				continue
			check[nx][ny] = check[x][y] + 1
			q.append((nx,ny))

q.append((sx,sy))
dist[sx][sy] = 0
while q:
	x,y = q.popleft()
	for k in range(4):
		nx, ny = x + dx[k], y + dy[k]
		if 0<=nx<r and 0<=ny<c:
			if dist[nx][ny] != -1:
				continue
			if a[nx][ny] == 'X':
				continue
			if check[nx][ny] != -1 and dist[x][y]+1 >= check[nx][ny]:
				continue
			dist[nx][ny] = dist[x][y]+1
			q.append((nx,ny))

if dist[end_x][end_y] == -1:
	print("KAKTUS")
else:
	print(dist[end_x][end_y])