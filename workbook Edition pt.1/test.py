mybin = bin(14)
print(type(mybin))
mybin = int(mybin[2:])
mybin = format(mybin, '0={}'.format(5))
print(mybin)

mybin2 = bin(3)
print(mybin2)
print(type(mybin2))
mybin2 = mybin2[2:]
print(mybin2.zfill(5))
print(mybin2.rjust(5, '0'))

a = "501"
print(a.zfill(5))
print(a.rjust(5, '0'))
