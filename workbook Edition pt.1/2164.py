import sys
import math

n = int(sys.stdin.readline())
# #queue alg
# q = [i for i in range(1,n+1)]
# index = -1
# result = 0
# while q:
# 	index = (index + 1) % len(q)
# 	result = q[index]
# 	q.pop(index)
# print(result)

#log
cal = int(math.log(n,2))
result = 2*(n - 2**cal)
if result == 0:
	print(n)
else:
	print(result)