n= int(input())
# x,y = 1,1
# change = 0
# for i in range(1,n):
# 	if x == 1 and x<=y and change == 0:
# 		y += 1
# 		change = 1
# 	elif y == 1 and x>=y and change == 1:
# 		x += 1
# 		change = 0

# 	elif change == 0:
# 		x -= 1
# 		y += 1
# 	elif change == 1:
# 		x += 1
# 		y -= 1
# print("%d/%d" % (x,y))

# 1 2
# 2 3
# 3 3
# 4 4
# 5 4
# 6 4
# 7 5
# 8 5
# 9 5
# 10 5

re = 0
cnt = 0
for i in range(n):
	cnt +=1
	re +=i
	if re >= n:
		re -=i-1
		cnt -=1
		break
if cnt == 1:
	x = 1
	y = 1
elif n ==2:
	x = 1
	y = 2

elif cnt%2 == 1:
	x = cnt
	y = 1
	for i in range(n-re):
		x -= 1
		y += 1

elif cnt%2 == 0:
	x = 1
	y = cnt
	for i in range(n-re):
		x += 1
		y -= 1

print("%d/%d" % (x,y))




