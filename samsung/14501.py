# -*- coding: utf-8 -*-

# day= int(input())
# arr = [[0 for col in range(2)] for row in range(day)]
# # list2 = [[0]*3 for i in range(3)]
# for i in range(day):
# 	ti, pi = input().split()
# 	arr[i][0] = int(ti)
# 	arr[i][1] = int(pi)

# for i in range(day-1,-1,-1):
# 	print("i:{} day:{} value:{}".format(i, i+1, arr[i][0]+i+1))
# 	if(arr[i][0]+i+1 > day+1):
# 		arr[i][1] = 0

# print(arr)


# tmp_arr = arr
# print(tmp_arr)

# result = [0]*day
# for j in range(day):
# 	sum_pi = 0 #날짜 더하는 변수
# 	i = 0
# 	print(j)
# 	while(i < day):
# 		print(i)
# 		print("i:{} day:{} value:{}".format(i, i+1, arr[i][0]+i+1))
# 		if(arr[i+j][0]+i+1 <= day+1):
# 			sum_pi += arr[i][1]
# 			i += arr[i][0]
# 		else:
# 			break
# 	result[j] = sum_pi
# print(result)

import sys
def solve(n, t, p):
	dp = [0 for i in range(n)]

	if t[n-1] == 1:
		dp[n-1] = p[n-1]

	for i in range(n-2, -1,-1):
		day = i + t[i]

		if day == n: #p[i] 하나하는게 더 크냐? dp[i+1]뒤에 것 하는게 더 크냐?
			dp[i] = max([p[i], dp[i+1]])
		elif day < n: #i번째 끝나고 dp[day]도 할 수 있으니까 둘이 더한게 더 크냐? or i+1한게 더 크냐?
			dp[i] = max([p[i] + dp[day], dp[i+1]])
		elif day > n:# 넌 이미 죽어있다.
			dp[i] = dp[i+1]
	print(dp[0])

if __name__ == '__main__':
	n = int(sys.stdin.readline())
	t = []
	p = []

	for i in range(n):
		ti, pi = map(int, sys.stdin.readline().split())
		t.append(ti)
		p.append(pi)
	solve(n,t,p)
