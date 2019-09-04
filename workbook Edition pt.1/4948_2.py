# MAX = 11
# num = [x for x in range(MAX+1) if x%2]
MAX = 123456*2
num = [1 for x in range(MAX+1)]
num[0],num[1] = 0,0
for i in range(2,MAX+1):
	j = 2
	while(MAX>=i*j):
		num[i*j] = 0
		j += 1
while 1:
	n = int(input())
	if n <= 0:
		break
	print(sum(num[n+1:n*2+1]))