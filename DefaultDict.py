Dict={1:'Geeks',2:'For',3:'Geeks'}
print("Dictionary :")
print(Dict)
print(Dict[1])
#print(Dict[4])
from collections import defaultdict
def def_value():
    return "Not Present"
d=defaultdict(def_value)
d['a']=1
d['b']=2
print(d['a'])
print(d['c'])
#default factry
d1=defaultdict(lambda:"Not Present")
d1['a']=1
d1['b']=2
print(d['a'])
print(d['c'])

