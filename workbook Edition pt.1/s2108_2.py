import sys;input();p=print
s=[0]*8003
l=0
for i in sys.stdin:s[int(i)+4000]+=1;l+=1.
p(round(sum((i-4000)*s[i]for i in range(8003))/l))
ll=l//2
for i in range(8003):
    ll-=s[i]
    if(ll < 0):
        p(i-4000)
        break
p(s.index(max(s),1+s.index(max(s))*(s.count(max(s))>1))-4000)
#http://blog.daum.net/bioinf/6543752
# p()
# p(1+s.index(max(s))*(s.count(max(s))>1))
# p((s.count(max(s))>1))
# p()
mn,mx=0,0
for i in range(8003):
    if(s[i]):
        mn=i
        break
for i in range(8002,-1,-1):
    if(s[i]):
        mx=i
        break
p(mx-mn)