from sys import stdin

n = int(stdin.readline())
dp = [[0]*10 for _ in range(n+1)]
mod = 10007

def sol():
	for i in range(10):
		dp[1][i] = 1
	for i in range(2,n+1):
		for j in range(9,-1,-1):
			for k in range(j,-1,-1):
				dp[i][j] += dp[i-1][k]
			dp[i][j] %= mod
sol()
print(sum(dp[n])%mod)
# print(dp)