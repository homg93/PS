# n = int(input())
# i =1
# mysum = [1]
# while(mysum[-1]<n):
# 	if i%6 == 0:
# 		mysum.append(mysum[-1]+i)
# 	i+=1
# print(len(mysum))
i,sum = 1,1
n = int(input())
while(sum <n):
    sum += (6 * i)
    i +=1
print(i)
