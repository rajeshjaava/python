squares=list(map(lambda x:x**2,range(10)))
print(squares)
#same as like below
sq=[x**2 for x in range(10)]
print(sq)
#form3
print([(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y])
vec=[1,2,3,4,5,6,7]
print([x*2 for x in vec] )
print(vec)
from math import pi
print([str(round(pi,x) for x in range(1,6))])
#matrix
matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
print([[row[i] for row in matrix ] for i in range(4)])

#del statement
a=[1,2,3,4,5,6,7]
del a[1]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a
# error print(a)