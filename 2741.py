a = int(input())
if(a <= 100 and a>=1):
	for i in range(1,a+1):
		for j in range(i):
			print('*',end="")
		print()