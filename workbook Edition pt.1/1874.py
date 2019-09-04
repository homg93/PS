import sys

n = int(sys.stdin.readline())
a=[]
for _ in range(n):
	snum = int(sys.stdin.readline())
	a.append(snum)

stack = []
scarr = []
i,j=0,1
while i < n:
	if a[i] < j:
		if stack and a[i] == stack[-1]:
			stack.pop()
			scarr.append('-')
			i +=1
		else:
			break
	elif a[i] >= j:
		stack.append(j)
		scarr.append('+')
		j += 1
if stack:
	print('NO')
else:
	for sc in scarr:
		print(sc)