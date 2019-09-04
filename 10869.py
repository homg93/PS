a,b,c = input().split()
A = int(a)
B = int(b)
C = int(c)

r1 = (A+B)%C
r2 = (A%C + B%C)%C
r3 = (A*B)%C
r4 = (A%C*B%C)%C
print("%d\n%d\n%d\n%d" % (r1,r2,r3,r4))
# a,b = input().split()
# a = int(a)
# b = int(b)
# add = a+b
# subtraction = a-b
# multiplication = a*b
# division = a//b
# rest = a%b
# print(add)
# print(subtraction)
# print(multiplication)
# print(division)
# print(rest)
