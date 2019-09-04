import sys

iron = sys.stdin.readline().rstrip()
a = ["("]
cnt_i = 0
cnt_r = 0

for i in range(1,len(iron)):
	if iron[i] == ")":
		a.pop()
		if iron[i-1] == "(":
			cnt_r += 1
			cnt_i += len(a)
		else:
			cnt_i += 1
	else:
		a.append("(")
print(cnt_i)