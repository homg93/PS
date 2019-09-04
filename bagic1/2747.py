from sys import stdin

def fibo(n):
	if a[n] != -1:
		return a[n]
	a[n] = fibo(n-1) + fibo(n-2)
	return a[n]

n = int(stdin.readline())
a = [-1 for i in range(n+1)]
a[0],a[1] = 0,1
print(fibo(n))