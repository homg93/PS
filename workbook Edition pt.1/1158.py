import sys
n, k = map(int,sys.stdin.readline().split())
q = []
cnt = 0
print('<',end='')
for i in range(n):
	three = 0
	while three<3:
		cnt+=1
		three+=1
		if n < cnt:
			cnt = 1
		if cnt in q:
			three-=1
	print(cnt, end='')
	if i != n-1:
		print(', ',end='')
	q.append(cnt)

print('>',end='')
