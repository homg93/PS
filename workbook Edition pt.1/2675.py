# import sys

# t = int(input())
# mylist = []

# for i in range(t):
# 	mystr = ''
# 	s,r = map(str, sys.stdin.readline().split())
# 	s = int(s)

# 	for j in range(len(r)):
# 		for k in range(s):
# 			mystr += r[j]
# 	mylist.append(mystr)


# for i in range(len(mylist)):
# 	print(mylist[i])

# exec("r,_,*s=input();print(''.join(i*int(r)for i in s));"*int(input()))
# exec("r,_,*s=input();print(s);"*int(input()))
# exec("n=10;print(i+i for i in range(1,n));")
# n=10
# print(''.join(i*int(r)for i in s));
exec("n=10;print(sum([i for i in range(1,n)]));")
# print((i*int(r) for i in s));
# r,_,*s=input()
# exec("a = [i for i in range(10)]")
