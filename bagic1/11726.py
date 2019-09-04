from sys import setrecursionlimit
setrecursionlimit(100000)
n = int(input())
d = [0 for _ in range(n+1)]
def dp(n):
	if n <= 2:
		return n
	if d[n] != 0:
		return d[n]
	d[n] = dp(n-1) + dp(n-2)
	return d[n]
print(dp(n)%10007)
