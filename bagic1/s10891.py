n=int(input())
L=sorted(list(map(int,input().split())))
R=[]
for i in range(n//2):
    if i%2 == 0:
        R.insert(0,L[-1-i])
        R.append(L[i])
    else:
        R.insert(0,L[i])
        R.append(L[-1-i])
print(R)
print(L)
r = 0
for i in range((n//2)*2-1):
    r+=abs(R[i]-R[i+1])
if n%2==0:
    print(r)
else:
    print(max(r+abs(L[n//2]-R[0]),r+abs(L[n//2]-R[-1])))
    print(min(r+abs(L[n//2]-R[0]),r+abs(L[n//2]-R[-1])))

# r = [1,2,3]
# l = [-1,-2,-3]
# i = 2
# r.insert(0,l[-1-i])
# print(r)