n = int(input())
cnt = 0

for i in range(n+1):
	a = []
	judge = 0

	if i <= 99:
		cnt = i
	if i>=100:
		t = i
		sp = len(str(i))
		while(t>0):
			a.append(t%10)
			t //= 10

		for j in range(sp-2):
			if (a[j] - a[j+1]) == (a[j+1] - a[j+2]):
				judge += 1

		if( judge == sp-2):
			cnt +=1
print(cnt)