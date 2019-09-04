from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
r, c = map(int,(input().split()))
a = [list(input()) for _ in range(r)]

dist = [[-1]*c for _ in range(r)]
check = [[-1]*c for _ in range(r)]

q = deque()

aq = deque()
ok = 1
for i in range(r):
    for j in range(c):
        if a[i][j] == '*':
            check[i][j] = 0
            aq.append((i,j))
        elif a[i][j] == 'S':
            dist[i][j] = 0
            q.append((i,j))
        elif a[i][j] == 'D':
            end_x, end_y = i,j
while aq:
    x,y = aq.popleft()
    for k in range(4):
        ax, ay = x+dx[k], y+dy[k]
        if 0<=ax<r and 0<=ay<c:
            if a[ax][ay] == '.' and check[ax][ay] == -1:
                check[ax][ay] = check[x][y] + 1
                aq.append((ax,ay))

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

# for cc in dist:
#   print(cc)
# print("===================")

# for cc in check:
#   print(cc)

if dist[end_x][end_y] == -1:
    print("KAKTUS")
else:
    print(dist[end_x][end_y])