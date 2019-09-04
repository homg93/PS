# n = int(input())

# stair = []

# for i in range(n):
#     temp = int(input())
#     stair.append(temp)

# dp = []

# dp.append(stair[0]) # 첫 번째
# dp.append(stair[1] + dp[0]) # 두 번째
# dp.append(max(stair[2] + stair[0], stair[2] + stair[1]))

# for i in range(3, n):
#     dp.append(max(stair[i] + dp[i - 2], stair[i] + stair[i - 1] + dp[i - 3]))

# print(stair)
# print(dp)
# print(dp[n - 1])

import sys

s=[]
n=int(sys.stdin.readline())
for x in range(n):
    s.append(int(sys.stdin.readline()))

d1=[s[0],s[0]+s[1]]
d2=[0,s[1]]

for x in range(2,n):
    d1.append(d2[x-1]+s[x])
    d2.append(max(d1[x-2]+s[x],d2[x-2]+s[x]))

print(max(d1[n-1],d2[n-1]))