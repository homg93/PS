import sys

def stairs(n):
	if n < 3:
		return sum(a)
	dp.append(a[0])
	dp.append(a[1]+dp[0])
	dp.append(a[2]+max(a[0],a[1]))
	for i in range(3,n):
		dp.append(a[i]+max(dp[i-2],a[i-1]+dp[i-3]))
	return dp[-1]

n = int(sys.stdin.readline())
a = []
for _ in range(n):
	a.append(int(sys.stdin.readline()))
dp = []

print(stairs(n))
