n = int(input())
a = list(map(int,input().split()))
d = [0]*n
v = [-1]*n
for i in range(n):
    d[i] = 1
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j]+1:
            d[i] = d[j]+1
            v[i] = j
ans = max(d)
print(ans)
p = [i for i,x in enumerate(d) if x == ans][0]
def go(p):
    if p == -1:
        return
    go(v[p])
    print(a[p],end=' ')
go(p)
print()