import sys

a = []
t = int(sys.stdin.readline())

for _ in range(t):
	n = int(sys.stdin.readline())
	if n == 0:
		a.pop()
	else:
		a.append(n)
print(sum(a))