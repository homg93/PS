from sys import stdin

str1 = stdin.readline().rstrip()
str2 = stdin.readline().rstrip()
len1, len2 = len(str1)+1,len(str2)+1
dp = [[0 for _ in range(len1)] for _ in range(len2)]

for i in range(1,len2):
	for j in range(1,len1):
		if str1[j-1] == str2[i-1]:
			dp[i][j] = dp[i-1][j-1] + 1
		else:
			dp[i][j] = max(dp[i][j-1],dp[i-1][j])
print(max(max(dp)))
# for arr in dp:
# 	print(arr)

##s9251.py
# from sys import stdin

# def dp(p1,p2):
#     memo = [0 for _ in range(len(p2)+1)]
#     for i in range(len(p1)):
#         temp = [0]
#         for j in range(len(p2)):
#             temp.append(memo[j]+1 if p1[i]==p2[j] else max(temp[j],memo[j+1]))
#         memo = temp
#     return memo[-1]

# P1 = stdin.readline().rstrip()
# P2 = stdin.readline().rstrip()

# print(dp(P1,P2))