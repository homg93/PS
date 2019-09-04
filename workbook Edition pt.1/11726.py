import sys

# def tile(n):
# 	if a[n] != 0:
# 		return a[n]
# 	if n == 1:
# 		return 1
# 	elif n == 2:
# 		return 2
	
# 	a[n] = tile(n-1)+tile(n-2)
# 	return a[n]
import sys

def tile2(n):
	for i in range(2,n):
		a[i] = a[i-1] + a[i-2]
	return a[n-1]

n = int(sys.stdin.readline())
a = [0 for _ in range(n+1)]
a[0],a[1] = 1,2
print(tile2(n)%10007)
