# a = int(input())
# if(a <= 100 and a>=1):
# 	for i in range(1,a+1):
# 		print(" "*(5-i), end="")
# 		print("*"*i)
a=int(input())
for i in range(1,a+1):
    print(" "*(a-i) + "*"*i)