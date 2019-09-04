from sys import setrecursionlimit
setrecursionlimit(1000000)

dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,-1,1,1,-1,-1,1]
ans = []
def bfs(x,y,cnt):
	q = []
	q.append([x,y])
	check[x][y] = cnt
	while(len(q)):
		x,y = q.pop(0)
		for k in range(8):
			nx,ny = x + dx[k], y + dy[k]
			if 0<=nx<h and 0<=ny<w:
				if check[nx][ny] == 0 and a[nx][ny] == 1:
					q.append([nx,ny])
					check[nx][ny] = cnt

def dfs(x,y,cnt):
	if check[x][y] == 0:
		check[x][y] = cnt
	else:
		return
	for k in range(8):
		nx,ny = x + dx[k], y + dy[k]
		if 0<=nx<h and 0<=ny<w:
			if a[nx][ny] == 1 and check[nx][ny] == 0:
				dfs(nx,ny,cnt)

while(True):
	w,h = map(int,input().split())
	if w == 0 and h == 0:
		break
	a = [list(map(int,list(input().split()))) for _ in range(h)]
	check = [[0]*w for _ in range(h)]
	cnt = 0
	for i in range(h):
		for j in range(w):
			if a[i][j] == 1 and check[i][j] == 0:
				cnt +=1
				# bfs(i,j,cnt)
				dfs(i,j,cnt)
	ans.append(cnt)
	# print("check")
	# for cc in check:
	# 	print(cc)
print("\n".join(map(str,ans)))