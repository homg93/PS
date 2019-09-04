from functools import reduce
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
start = deque()
def bfs(q):
	while len(q):
		x,y = q.popleft()
		for k in range(4):
			nx,ny = x + dx[k], y + dy[k]
			if 0<=nx<h and 0<=ny<w:
				if dist[nx][ny] == -1 and a[nx][ny] == 0:
					q.append((nx,ny))
					dist[nx][ny] = dist[x][y]+1

w,h = map(int,input().split())
a = [list(map(int,list(input().split()))) for _ in range(h)]

dist = [[-1]*w for _ in range(h)]
cnt = 0
for i in range(h):
	for j in range(w):
		if a[i][j] == 1:
			start.append((i,j))
			dist[i][j] = 0
bfs(start)
# for cc in dist:
# 	print(cc)
# ans = max([max(row) for row in dist])
# for i in range(h):
#     for j in range(w):
#         if a[i][j] == 0 and dist[i][j] == -1:
#             ans = -1
# print(ans)
dist = reduce(lambda x,y: x+y,dist)
if dist.count(-1) == reduce(lambda x,y: x+y,a).count(0):
	print(-1)
else:
	print(max(dist))