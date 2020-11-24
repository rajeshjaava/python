import collections
dict1={'a':1,'b':2}
dict2={'c':3,'d':4}
chain=collections.ChainMap(dict1,dict2)
print("All chain map content")
print(chain)
# reversing the ChainMap 
chain.maps = reversed(chain.maps)  
print(chain)
