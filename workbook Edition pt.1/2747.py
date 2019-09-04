import sys

def pibo(n):
	if a[n] != -1:
		return a[n]
	a[n] = pibo(n-1)+pibo(n-2)
	return a[n]

n = int(sys.stdin.readline())
a =[-1 for _ in range(n+1)]
a[0],a[1] = 0,1
print(pibo(n))

################

import sys

def pibo(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif a[n-1] == -1:
		a[n-1] = pibo(n-1)
	elif a[n-2] == -1:
		a[n-2] = pibo(n-2)
	return a[n-1]+a[n-2]

n = int(sys.stdin.readline())
a =[-1 for _ in range(n+1)]
a[0],a[1] = 0,1
pibo(n+1)
print(a[-1])