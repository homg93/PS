from sys import stdin
n = int(stdin.readline())
d = [-1 for _ in range(n+1)]
def go(n):
	if n == 1:
		return 0
	if d[n] > 0:
		return d[n]
	d[n] = go(n-1) + 1
	if n % 3 == 0:
		d[n] = min(d[n],go(n//3)+1)
	if n % 2 == 0:
		d[n] = min(d[n],go(n//2)+1)
	return d[n]
print(go(n))