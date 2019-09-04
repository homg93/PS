from sys import stdin

def sub_max(a,n):
	tot = 0
	for i in range(n-1):
		tot += abs(a[i] - a[i+1])
	return tot

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
	return a

n = int(stdin.readline())
a = list(map(int,stdin.readline().split()))
tot_max = 0
a = sorted(a)
# print(a)
while next_permutation(a,n):
	tmp = sub_max(a,n)
	if tot_max < tmp:
		tot_max = tmp
print(tot_max)