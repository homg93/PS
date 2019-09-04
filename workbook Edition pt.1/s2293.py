import sys
 
n, k = list(map(int, sys.stdin.readline().split()))
value = []
for i in range(n):
	temp = int(sys.stdin.readline())
	value.append(temp)
dp = [100001 for i in range(k+1)]
dp[0] = 0
for i in value:
	for j in range(i, k+1):
		if dp[j] > dp[j-i]+1:
			dp[j] = dp[j-i]+1
if dp[k] > 100000:
	print(-1)
else:
	print(dp[k])
print(dp)