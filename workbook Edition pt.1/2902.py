name = input()
len_name = len(name)
for i in range(len_name):
	if ord(name[i]) >= 65 and ord(name[i]) <= 90:
		print(name[i],end='')

