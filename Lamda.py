
adder= lambda x,y:x+y
print(adder(1,2))
x="some kind of lamda"
(lambda x: print(x))(x)
#filters
sequences=[10,2,5,6,7,4,3]
filtered_result=filter(lambda x: x>4,sequences)
print(list(filtered_result))
#map
map_result=map(lambda x: x*2,sequences)
print(list(map_result))
#reduce
from functools import reduce
product=reduce(lambda x,y:x*y,sequences)
print(product)