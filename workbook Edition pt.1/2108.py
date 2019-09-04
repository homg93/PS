import sys
from collections import Counter

n = int(sys.stdin.readline())
a = []
sum_a = 0
for _ in range(n):
	w = int(sys.stdin.readline())
	a.append(w)
	sum_a += w

print('%.0f'%(sum_a/n))
# print(round(sum_a/n))

if n == 1:
	print(a[0])
	print(a[0])
	print(0)
	sys.exit()

a = sorted(a)
print(a[n//2])

cnt = Counter(a)
cnt = sorted(cnt.items(), key = lambda x: -x[1])

if cnt[0][1] == cnt[1][1]:
	print(cnt[1][0])
else:
	print(cnt[0][0])
print(a[-1] - a[0])