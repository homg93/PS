# -*- coding: utf-8 -*-
d = [0]*100
def dp(x):
	if x == 1 or x == 2:
		return 1
	if(d[x] !=0):
		return d[x]
	d[x] = dp(x-1) + dp(x-2)
	return d[x]

if __name__ == '__main__':
	print(dp(30))


# def dp(x):
# 	if x == 1 or x == 2:
# 		return 1
# 	return dp(x-1) + dp(x-2)

# if __name__ == '__main__':
# 	print(dp(30))