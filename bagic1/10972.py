from sys import stdin

def next_permutation(a,n):
	i = n-1
	while(i > 0 and a[i-1] >= a[i]):
		i -= 1
	if i == 0:
		return False

	j = n-1
	while(a[j] <= a[i-1]):
		j -= 1
	a[j], a[i-1] = a[i-1],a[j]

	j = n-1
	while i < j:
		a[i], a[j] = a[j],a[i]
		i +=1; j -=1
	return True

n = int(stdin.readline())
a = list(map(int,stdin.readline().split()))

if next_permutation(a,n):
	for k in a:
		print(k,end=' ')
else:
	print(-1)