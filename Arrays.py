import array as myarray
abc=myarray.array('d',[2.5,4.8,7.8,8,9])
print(abc)
print("Array first element is :",abc[-1])
abc.insert(2,9.0)
print(abc)
abc.pop(2)
print(abc)
abc.remove(8.0)
print(abc)
abc.reverse()
print(abc)
for x in abc:
    print(x)