# import sys
# n = int(input())

# def warp(dist):
# 	minN = powN = maxN = cnt = 0; n = 1
# 	while 1:
# 		powN = n*n
# 		minN = powN - n +1
# 		maxN = powN + n
# 		if minN <= dist and dist<=maxN:
# 			if minN<=dist and dist<=powN:
# 				cnt = (n<<1) - 1
# 			else:
# 				cnt = n<<1
# 			break
# 		n+=1
# 	return cnt


# for i in range(n):
# 	x, y = map(int, sys.stdin.readline().split())
# 	print(warp(y-x))

import sys;r=sys.stdin.readline;n=int(r())
for _ in range(n):
	x,y=map(int,r().split());sq=int((y-x-1)**0.5)
	print(sq)
	if y-x>sq*sq+sq:print(2*sq+1)
	else:print(2*sq)