import sys

t = int(sys.stdin.readline())

prime = [1 for i in range(10001)]
prime[0],prime[1] = 0,0

for i in range(2,101):
	j = 2
	while(10000 >= i*j):
		prime[i*j] = 0
		j += 1

mcal = []
for _ in range(t):
	n = int(sys.stdin.readline())
	for i in range(1,n//2+1):
		if prime[i] == 1 and n > i:
			if prime[n-i] == 1:
				mcal.append([i,n-i])

	print("%d %d" %(mcal[-1][0],mcal[-1][1]))
				