n = int(input())
a = list(map(int,input().split()))
d = [[0]*2 for _ in range(n)]
for i in range(n):
	d[i][0] = a[i]
	d[i][1] = a[i]
	if i == 0:
		continue
	if d[i][0] < d[i-1][0] + a[i]:
		d[i][0] = d[i-1][0] + a[i]
	d[i][1] = max(d[i-1][0],d[i-1][1]+a[i])
ans = [max(row) for row in d]
print(max(ans))