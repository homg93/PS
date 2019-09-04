import sys

def sticker(n,a):
	dp = [[0]*3 for _ in range(n)]
	dp[0][1],dp[0][2]= a[0][0],a[1][0]

	for i in range(1,n):
		dp[i][0] = max(dp[i-1])
		dp[i][1] = max(a[0][i]+dp[i-1][2],a[0][i] +dp[i-1][0])
		dp[i][2] = max(a[1][i]+dp[i-1][1],a[1][i] +dp[i-1][0])
	return max(dp[n-1])

t = int(sys.stdin.readline())
for _ in range(t):
	n = int(sys.stdin.readline())
	a = []
	a.append(list(map(int, sys.stdin.readline().split())))
	a.append(list(map(int, sys.stdin.readline().split())))
	print(sticker(n,a))


# from sys import stdin
# read = lambda: stdin.readline().rstrip()
# for _ in range(int(read())):
#     n = int(read())
#     a, b = 0, 0
#     c, d = 0, 0
#     arr1 = tuple(map(int, read().split()))
#     arr2 = tuple(map(int, read().split()))
#     for i in range(n):
#         a, b, c, d = b, max(c, d) + arr1[i], d, max(a, b) + arr2[i]
#     print(max(b, d))