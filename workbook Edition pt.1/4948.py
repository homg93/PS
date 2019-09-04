import math
def isPrime(num):
	if num == 1: return False

	n = int(math.sqrt(num))
	for k in range(2, n+1):
		if num % k == 0: return 0
	return True

while (1):
	m = int(input())
	cnt = 0
	if(m==0):
		break
	n = m+m
	for k in range(m+1,n+1):
		if k ==2:
			cnt +=1
		if k % 2:
			if isPrime(k) : cnt += 1

	print(cnt)

n = int(input())
n2 = n+n
