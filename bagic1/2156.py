from sys import stdin

n = int(stdin.readline())
a = [0]
for _ in range(n):
	a.append(int(stdin.readline()))
dp = [0]*(n+1)
dp[1] = a[1]
if n >= 2:
	dp[2] = a[1]+a[2]
for i in range(3,n+1):
	dp[i] = dp[i-1]
	dp[i] = max(dp[i],dp[i-2]+a[i])
	dp[i] = max(dp[i],dp[i-3]+a[i]+a[i-1])
print(dp[n])
