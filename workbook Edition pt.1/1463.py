import sys
def mym(n):
	for i in range(4,n+1):
		a.append(a[i-1]+1)
		if i % 2==0:
			a[i] = min(a[i],a[i//2]+1)
		if i % 3==0:
			a[i] = min(a[i],a[i//3]+1)
	return a[n]

n = int(sys.stdin.readline())
a = [0,0,1,1]
print(mym(n))

###
save = {1:0, 2:1}
def frog(n):
    if n in save:
        return save[n]
    m = 1+min(frog(n//2)+n%2, frog(n//3)+n%3)
    save[n] = m
    return m

n = int(input())
print(frog(n))