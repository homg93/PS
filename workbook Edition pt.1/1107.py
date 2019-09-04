import sys

n = input()
m = int(input())
err = list(map(int,sys.stdin.readline().split()))
cor = [i for i in range(10)]
# for i in range(len(err)):
# 	cor[err[i]] = -1
for i in range(len(err)):
	cor.remove(err[i])
print(cor)

cnt = 0
init =100
temp = []
cal = []
goal = int(n)



for i in range(len(n)):
	temp.append(int(n[i]))
	if int(n[i]) not in cor:
		for j in range(len(cor)):
			n_ten = cor[j]*pow(10,len(n)-i-1)
			print(n_ten)
			temp[i] = n_ten
			aaa =str(temp)
			print(aaa)


			# print(abs(goal-int(temp)))
			# cal.append(())
		# print(cal)
# for i in range(len(cor)):
# 	if int(n[i])
# 	print(abs())

# while(init!=goal):
# 	if init > n:
# 		init -= 1
# 		cnt +=1
# 	else:
# 		init +=1
# 		cnt +=1


# print(cnt)

