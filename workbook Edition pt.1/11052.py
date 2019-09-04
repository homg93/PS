import sys

def maxdp(n,a):
	dp = [0 for _ in range(n+1)]
	dp[0],dp[1] = 0,a[1]
	for i in range(1,n+1):
		for j in range(i,n+1):
			dp[j] = max(a[i]+dp[j-i],dp[j]) 
			# print("dp[%d] = %d"%(j,dp[j]))
	return dp[n]

n=int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a = [0]+a
print(maxdp(n,a))

## s11052.py
# N = int(input())
# P = input().split()
# Q = [int(num) for num in P]
# R = [0]+Q

# for i in range(1, N+1):
# 	R[i] = max(R[j] + R[i-j] for j in range(i//2, i+1))

# print(R[N])