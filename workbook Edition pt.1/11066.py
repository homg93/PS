from sys import stdin

t = int(stdin.readline())

for _ in range(t):
	k = int(stdin.readline())
	a = list(map(int,stdin.readline().split()))
	lena = len(a)
	temp = 0
	while(lena > 1):
		a.sort()
		lena2 = (lena//2)*2
		for j in range(0,lena2,2):
			a.append(a[j]+a[j+1])
			print(a[j]+a[j+1])
		a = a[lena2:]
		print(a)
		temp += sum(a)
		lena = len(a)
	print(temp)


