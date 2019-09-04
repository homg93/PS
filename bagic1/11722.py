n = int(input())
a = list(map(int,input().split()))
inc = [0]*n
dec = [0]*n
for i in range(n):
	inc[i] = 1
	for j in range(i):
		if a[i] > a[j] and inc[i] < inc[j]+1:
			inc[i] = inc[j]+1
		
for i in range(n-1,-1,-1):
	dec[i] = 1
	for j in range(i,n):
		if a[i] > a[j] and dec[i] < dec[j]+1:
			dec[i] = dec[j]+1
m = [inc[i]+dec[i]-1 for i in range(n)]
print(max(m))