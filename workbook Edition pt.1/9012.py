import sys

t = int(sys.stdin.readline())

for _ in range(t):
	n = sys.stdin.readline().rstrip()
	cnt = 1
	cal = []

	for i in range(len(n)):
		if n[i] == "(":
			cal.append(1)
		else:
			if len(cal):
				cal.pop()
			else:
				cnt=0
				break
	if len(cal) !=0:
		cnt = 0
	if cnt==1:
		print("YES")
	else:
		print("NO")


t = int(sys.stdin.readline())

for _ in range(t):
	n = list(sys.stdin.readline().rstrip())
	cal = []
	cnt = 1

	for i in range(len(n)):
		temp = n.pop()
		if temp == ')':
			cal.append(temp)
		else:
			if len(cal)!=0:
				cal.pop()
			else:
				cnt = 0
				break
	if len(cal) !=0:
		cnt = 0
	if cnt:
		print('YES')
	else:
		print('NO')

