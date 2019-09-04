n= int(input())

def star11(n):

	for i in range(n):
		for j in range(n+i):
			if j == n+i-1:
				print("*",end='')
				print("")
			elif i % 3 == 2:
				if j >= n-i-1 and j <= n+i-2:
					print("*",end='')
				else:
					print(" ",end='')
			elif j == n-i-1:
				print("*",end='')
			else:
				print(" ",end='')
			# else:
			# 	star11(n//3)
		# print("")


# for i in range(n):
# star11(n)

def star11_2(i,j):
	print("i,j = %d, %d" %(i,j))
	if( i % 3 == 0):
		if j == n-i-1 or j == n+i-1:
			print("*",end='')
		else:
			print(" ",end='')
	if( i % 3 == 1):
		if j == n-i-1 or j == n+i-1:
			print("*",end='')
		elif j == n-i+1 or j == n+i-3:
			print("*",end='')
		else:
			print(" ",end='')
	if( i % 3 == 2):
		if j >= n-i-1 and j <= n+i-2:
			print("*",end='')
	print(" ",end='')
def star11_2(n,i,j):
	if i+j == n -1:
		print("*",end='')
	elif i+j == n+(2*i)-1:
		print("*",end='')
	else:
		print(" ",end='')
	# star11_2(n-i,i,j)

# star11_2(n-3,i,j)


for i in range(n):
	for j in range(n+i):
		star11_2(n,i,j)
	print("")
