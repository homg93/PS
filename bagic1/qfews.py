from sys import stdin
from collections import deque, Counter
from functools import reduce

n = int(stdin.readline())
a = [list(map(int,list(input()))) for _ in range(n)]
# a = [list(map(int,list(sys.stdin.readline()))) for _ in range(n)]
check = [[0 for i in range(n)] for j in range(n)]
cnt = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(i,j,cnt):
	q = []
	q.append([i,j])
	check[i][j] == cnt
	while len(q):
		x,y = q.pop(0)
		for k in range(4):
			nx = x+dx[k]
			ny = y+dy[k]
			if 0 <= nx < n and 0<= ny < n:
				if a[nx][ny] == 1 and check[nx][ny] == 0:
					q.append([nx,ny])
					check[nx][ny] = cnt

for i in range(n):
	for j in range(n):
		if a[i][j] == 1 and check[i][j] == 0:
			cnt += 1
			bfs(i,j,cnt)

ans = reduce(lambda x,y : x+y, check)
ans = [x for x in ans if x > 0]
# ans = list(filter(lambda x: x>0, ans))
ans = sorted(list(Counter(ans).values()))
print(cnt)
print('\n'.join(map(str,ans)))