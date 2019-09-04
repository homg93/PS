from sys import setrecursionlimit
setrecursionlimit(100000)
n = int(input())
a = []
for _ in range(n):
	a.append(int(input()))

d = [0 for _ in range(max(a)+1)]
d[0] = 1
def dp(n):
	if n < 0:
		return 0
	if d[n] != 0:
		return d[n]
	d[n] = dp(n-1) + dp(n-2) + dp(n-3)
	return d[n]
dp(max(a))
for i in range(n):
	print(d[a[i]]%1000000009)
