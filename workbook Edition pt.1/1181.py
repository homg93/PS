import sys
from collections import Counter
 
n = int(sys.stdin.readline())
dic = {}
for _ in range(n):
    temp = sys.stdin.readline().rstrip()
    mylen = len(temp)
    dic[temp] = mylen

cnt = sorted(dic.items())
cnt = sorted(cnt, key = lambda x: x[1])

for a,b in cnt:
	print(a)