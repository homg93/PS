L = [0,1,2,3,1,2,3,1]
target = 1
print([ i for i, x in enumerate( L ) if x == target ])
for i, x in enumerate( L ):
 print(i,x)