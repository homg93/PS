from sys import stdin

def next_permutation(a,n):
	i = n-1
	while(i > 0 and a[i-1] >= a[i]):
		i -= 1
	if(i == 0):
		return False

	j = n-1
	while(a[i-1] >= a[j]):
		j -= 1
	a[i-1], a[j] = a[j], a[i-1]

	j = n-1
	while(i<j):
		a[i], a[j] = a[j], a[i]
		i += 1; j -= 1
	return True

def tsp(w,a):
	global ans
	ok = True
	tot = 0
	
	for i in range(n-1):
		if w[a[i]][a[i+1]] == 0:
			ok = False
		else:
			tot += w[a[i]][a[i+1]]
	if ok and w[a[n-1]][a[0]] != 0:
		tot += w[a[n-1]][a[0]]
		if ans > tot:
			ans = tot
	
n = int(stdin.readline())
w = []
a = []
ans = 999999999

for i in range(n):
	w.append(list(map(int,stdin.readline().split())))
	a.append(i)

tsp(w,a)
while(next_permutation(a,n)):
	if a[0] != 0:
		break
	tsp(w,a)

print(ans)