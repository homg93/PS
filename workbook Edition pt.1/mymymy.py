from collections import Counter

data = [1,2,3,4,5]
s = [3,1,2,3,3,3]
#collections 모듈의 Counter() 메소드를 이용해서 data안의 원소들의 개수를 딕셔너리 형태로 저장
# cnt = Counter(data)
# print(cnt)
# test0 = sorted(cnt)
# test1 = sorted(cnt.items())
# test2 = sorted(cnt.items(), key=lambda x: (-x[0],x[1]))
# print(index(max(data)))
# print(data.index(max(data),5))
# print(data.count(max(data)))
print((max(s)))
print(s.index(max(s)))
print(s.count(max(s)))
print(s.count(max(s))>1)
print(1+s.index(max(s))*(s.count(max(s))>1))
print(s.index(3,5))
# print(s.index(max(s),1))
print(s.index(max(s),1+s.index(max(s))*(s.count(max(s))>1))-4000)

print(data.index(3,2))
print(data)
# cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
# cnt = sorted(cnt.items(), key=lambda x: -x[1])
# cnt = sorted(cnt.items(), key=lambda x: (-x[1],x[0]))

# cnt = sorted(cnt.items(), key=lambda x: -x[1], reverse=1)
# cnt = sorted(cnt.items(), key=lambda x: x[1])
# cnt = sorted(cnt.items(), key=lambda x: (x[1],x[0]))
# cnt = sorted(cnt.items(), key=lambda x: (-x[0],x[1]))
