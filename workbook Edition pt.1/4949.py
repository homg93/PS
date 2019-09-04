import sys


while 1:
	mystr = sys.stdin.readline().rstrip()
	if mystr == '.':
		break
	a = []
	is_bool = True

	for i in mystr:
		if i == ")":
			if not len(a) or a.pop() != '(':
				is_bool = False
				break
		elif i == "]":
			if not len(a) or a.pop() != '[':
				is_bool = False
				break
		elif i == "(":
			a.append(i)
		elif i == "[":
			a.append(i)
	# print(is_bool)
	# if len(a) != 0:
	# 	is_bool=False
	# print(not a)

	print('yes' if is_bool and not a else 'no')