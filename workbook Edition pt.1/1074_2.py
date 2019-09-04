import sys
n,r,c = map(int,sys.stdin.readline().split())
pow_2n = pow(2,n)
cnt = 0
change = 0
bi = [[0 for i in range(pow_2n)] for j in range(pow_2n)]

def list_print(n):
	n = pow(2,n)
	for i in range(n):
		for j in range(n):
			print('%.2d' % bi[i][j],end='')
		print()

def mybi(n,bi,i_start, j_start):
	global cnt
	global change

	print('{}, {}'.format(i_start,j_start))
	# print('{}, {}'.format(change, pow(4,n-1)))
	for i in range(i_start,i_start+2):
		for j in range(j_start,j_start+2):
			cnt += 1
			# bi[i][j] = cnt
			print('bi[{}][{}] = {}'.format(i,j,cnt))
	change +=1


i_start = 2
j_start = -2
# mybi(n,bi,i_start,j_start)

while (change < pow(4,n-1)):
	if change%4 == 0:
		i_start -=2 
		j_start	+=2
	elif change%4 == 1:
		j_start += 2
	elif change%4 == 2:
		j_start -= 2
		i_start += 2
	elif change%4 == 3:
		j_start += 2
	mybi(n,bi,i_start,j_start)

	# for i in range(change,change+2,2):
	# 	for j in range(change,change+2,2):
	# 		mybi(n,bi,i,j)

