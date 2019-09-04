import sys

# n = int(sys.stdin.readline())
def zoo(n):
	# a = [[0]*2 for i in range(n)]
	for i in range(3,n+1):
		dp.append((dp[i-1]+dp[i-2])*2 - dp[i-3]*2)
	return dp[n]

n = 6
dp = [0,2,6,16]
result = zoo(n)
print((result+1)%9901)

