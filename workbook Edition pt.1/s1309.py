# dp = [[0, 0, 0] for i in range(100010)]
# dp[1][0] = dp[1][1] = dp[1][2] = 1
# n = int(input())

# for i in range(2, n + 2):
#     dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901
#     dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901
#     dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901

# print(dp[n + 1][0])

a, b, c, d = 0, 3, 7, 17
for i in range(6):
    a, b, c, d = b, c, d, (2*d+c)%9901
    print("%d %d %d %d" %(a,b,c,d))
print(a)
