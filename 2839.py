n= int(input())
three = 0
five = n//5
n %= 5

while five>=0:
	print(five)
	if n%3 ==0:
		three=n//3; n%=3; break
	five -= 1; n+=5
print(n==0 and (five+three) or -1)
print("n =%d" % n)
print(five+three)
	# print(five+three)
# for i in range

# def suger():
# 	share5 = int(a/5)
# 	rest5  = a%5
# 	if(rest5 == 0):
# 		print(share5)
# 	else:
# 		share3 = int(rest5/3)
# 		rest3 = rest5%3
# 		result = share5 + share3
# 		if(rest3 == 0):
# 			print(result)
# 		else:
# 			if(a%3 == 0):
# 				print(int(a/3))
# 			else:
# 				print(-1)
# for()
# suger()