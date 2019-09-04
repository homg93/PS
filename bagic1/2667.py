from collections import deque, Counter
from functools import reduce
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(x, y, cnt):
	q = deque()
	q.append((x,y))
	check[x][y] = cnt
	while q:
		x, y = q.popleft()
		for k in range(4):
			nx,ny = x+dx[k], y+dy[k]
			if 0 <= nx < n and 0<= ny < n:
				if a[nx][ny] == 1 and check[nx][ny] == 0:
					q.append((nx,ny))
					check[nx][ny] = cnt
n = int(input())
a = [list(map(int,list(input()))) for _ in range(n)]
check = [[0]*n for _ in range(n)]
cnt = 
for i in range(n):
	for j in range(n):
		if a[i][j] == 1 and check[i][j] == 0:
			cnt += 1
			bfs(i,j,cnt)

ans = reduce(lambda x,y : x+y, check)
ans = [x for x in ans if x > 0]
ans = sorted(list(Counter(ans).values()))
print(cnt)
print('\n'.join(map(str,ans)))