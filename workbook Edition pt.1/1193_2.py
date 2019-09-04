# n= int(input())

# re = 0
# cnt = 0
# for i in range(n):
# 	cnt +=1
# 	re +=i
# 	if re >= n:
# 		re -=i-1
# 		cnt -=1
# 		break

# if cnt%2 == 1:
# 	print(cnt-(n-re),'/',n-re+1)

# elif cnt%2 == 0:
# 	print(n-re+1,'/',cnt-(n-re))


N=int(input());k=0;S=0;
while S<N: k+=1;S=int(k*(k-1)/2);
a=k-S+N-1; b=k-a;
if k%2: a,b=b,a;
print("%d/%d"%(b,a))
print(S)
