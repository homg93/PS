n = int(input())
d = [[0]*2 for _ in range(n+1)]
d[1][0] = 1
d[2][0] = 1

for i in range(3,n+1):
	for j in range(2):
		if j == 1:
			d[i][j] = d[i-1][j-1]
		else:
			d[i][j] = sum(d[i-1])
print(sum(d[n]))