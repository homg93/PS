from sys import stdin

def go(n,s,arr,tot,i):
	if s == tot and i == n:
		return 1
	if n <= i:
		return 0
	num = 0

	num += go(n,s,arr,tot+arr[i],i+1)
	num += go(n,s,arr,tot,i+1)

	return num

n ,s = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))
ans = go(n,s,a,0,0)
if s == 0:
	ans -=1
print(ans)