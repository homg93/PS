import sys

def rgb_st(n):
	# dp[0][0],dp[0][1],dp[0][2] = a[0][0],a[0][1],a[0][2]
	dp[0] = a[0]

	for i in range(1,n):
		dp[i][0] = a[i][0] + min(dp[i-1][1],dp[i-1][2])
		dp[i][1] = a[i][1] + min(dp[i-1][0],dp[i-1][2])
		dp[i][2] = a[i][2] + min(dp[i-1][0],dp[i-1][1])
	return min(dp[n-1])

n = int(sys.stdin.readline())
a = []
for _ in range(n):
	rgb = list(map(int,sys.stdin.readline().split()))
	a.append(rgb)
dp = [[0]*3 for _ in range(n)]
print(rgb_st(n))
print(dp)