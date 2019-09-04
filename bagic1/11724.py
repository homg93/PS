from sys import stdin

n,m = map(int, stdin.readline().split())
a = [[] for i in range(n+1)]
check = [0 for i in range(n+1)]

for i in range(m):
	d1,d2 = map(int, stdin.readline().split())
	a[d1].append(d2)
	a[d2].append(d1)


def dfs(x):
	check[x] = True
	# print(x,end=' ')
	for y in a[x]:
		if check[y] == 0:
			dfs(y)

cnt = 0
for i in range(1,n+1):
	if not check[i]:
		dfs(i)
		cnt += 1
print(cnt)
