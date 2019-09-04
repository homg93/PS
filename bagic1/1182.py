from sys import stdin

n ,s = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
ans = 0
for i in range(1,1<<n):
	tot = 0
	for k in range(n):
		if i&(1<<k):
			tot += a[k]
	if tot == s:
		ans +=1

print(ans)