import sys

def screat_map(n):
	mymap = []

	arr11 = list(map(int, sys.stdin.readline().split()))
	arr22 = list(map(int, sys.stdin.readline().split()))
	arr1 = [format(int(bin(x)[2:]), '0={}'.format(n)) for x in arr11]
	arr2 = [format(int(bin(x)[2:]), '0={}'.format(n)) for x in arr22]



	for i in range(n):
		mybin = bin(arr11[i] | arr22[i])
		mybin = int(mybin[2:])
		mybin = format(mybin, '0={}'.format(n))
		# mybin = format(int(mybin[2:]), '0={}'.format(n))
		print(mybin)
		ans = ''

		for j in range(n):
			if mybin[j] == '1':
				ans += '#'
			elif mybin[j] == '0':
				ans += ' '
		mymap.append(ans)
	print(mymap)
if __name__ == '__main__':
	n = int(sys.stdin.readline())
	screat_map(n)

# print(bin(2))