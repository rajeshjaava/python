#demonstrate ordered dictionary
from collections import OrderedDict
print("This is a Dict : \n")
d={}
d['a']=1
d['b']=2
d['c']=3
d['d']=4

for key,value in d.items():
    print(key,value)
print("\n ordered dictionary ")
od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4
od['e']=5
od['f']=6
od['g']=7
od['h']=8
od['i']=9
od.pop('h')
for key,value in od.items():
    print(key,value)