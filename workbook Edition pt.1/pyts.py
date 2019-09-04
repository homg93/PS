import sys
a = [1,1,9,1,1,1]
for _ in range(a.count(min(a))):
	print(a.index(min(a)))
	# print(a.pop(a.index(min(a))))


