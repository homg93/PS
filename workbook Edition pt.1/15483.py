from sys import stdin

def lc(str1,str2):
	len1, len2 = len(str1)+1,len(str2)+1
	dp = [[i+j for i in range(len1)] for j in range(len2)]

	if str1 == str2:
		return 0

	for i in range(1,len2):
		for j in range(1,len1):
			if str1[j-1] == str2[i-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = min(dp[i][j-1]+1,dp[i-1][j]+1)
				dp[i][j] = min(dp[i-1][j-1]+1,dp[i][j])
	return dp[len2-1][len1-1]

str1 = list(stdin.readline().rstrip())
str2 = list(stdin.readline().rstrip())

print(lc(str1,str2))
# dp = lc(str1,str2)
# for arr in dp:
# 	print(arr)
# print(min(dp[-1]))

s1, s2 = input(), input()
if len(s1) > len(s2):
    s1, s2 = s2, s1
dp = list(range(len(s1)+1))
for i, c2 in enumerate(s2):
    dp_=[i+1]
    for j, c1 in enumerate(s1):
        if c2 == c1:
            dp_.append(dp[j])
        else:
            dp_.append(1+min(dp[j],dp[j+1],dp_[-1]))
    dp=dp_
print(dp[-1])