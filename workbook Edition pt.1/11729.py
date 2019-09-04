n = int(input())
mlist = []
i = 0
def hanoi(num,a,b,c):
	global i
	i +=1
	print('{}: ({},{},{},{})'.format(i,num,a,b,c))
	if(num == 1):
		mlist.append([a,c])
	else:
		hanoi(num-1,a,c,b)
		mlist.append([a,c])
		hanoi(num-1,b,a,c)

hanoi(n,1,2,3)
print(len(mlist))
for a,b in mlist:
	print('{} {}'.format(a,b))