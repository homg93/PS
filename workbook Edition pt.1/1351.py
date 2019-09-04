import sys
def infinity_seq(n):
	if n == 0:
		return 1
	elif n in a:
		return a[n]
	a[n] = infinity_seq(n//p) + infinity_seq(n//q)
	return a[n]

n,p,q = map(int,sys.stdin.readline().split())
a = {}
print(infinity_seq(n))