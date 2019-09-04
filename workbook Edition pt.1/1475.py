N = input()

a = [0 for i in range(9)]
cnt = 0
for n in N:
	n = int(n)
	if n == 6 or n == 9:
		cnt += 1
		if a[6] ==0 :
			a[6] = 1
			cnt = 0
		elif cnt == 2:
			a[6] += 1
			cnt = 0
	else:
		a[n] += 1
# print(a)
print(max(a))

# c=input().count
# print(max(int(max(map(c,'01234578'))),(c('6')+c('9')+1)//2))