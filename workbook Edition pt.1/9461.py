# import sys

# def padovan(n):
# 	if n < 3:
# 		return 1
# 	elif n < 5:
# 		return 2
# 	if a[n-1] != 0:
# 		return a[n-1]
# 	a[n-1] = padovan(n-1)+padovan(n-5)
# 	return a[n-1]

# t = int(sys.stdin.readline())
# for _ in range(t):
# 	n = int(sys.stdin.readline())
# 	a = [0 for _ in range(n-1)]
# 	print(padovan(n-1))

import sys

def padovan(n):
	if n < 3:
		return 1
	elif n < 5:
		return 2
	if a[n-1] != 0:
		return a[n-1]
	a[n-1] = padovan(n-1)+padovan(n-5)
	return a[n-1]
	a.append(padovan(n-1)+padovan(n-5))
	return a[-1]

t = int(sys.stdin.readline())
for _ in range(t):
	n = int(sys.stdin.readline())
	a=[]
	print(padovan(n-1))
