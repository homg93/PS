from sys import stdin

def mydp(n,a):
	dp = a+([[0]*n])
	for i in range(1,n):
			dp[0][i] += max(dp[1][i-1],dp[2][i-1])
			dp[1][i] += max(dp[0][i-1],dp[2][i-1])
			dp[2][i] = max(dp[0][i-1],dp[1][i-1],dp[2][i-1])
	return max(dp[0][n-1],dp[1][n-1],dp[2][n-1])

T = int(stdin.readline())
for _ in range(T):
	n = int(stdin.readline())
	a = [list(map(int,stdin.readline().split())) for i in range(2)]
	print(mydp(n,a))