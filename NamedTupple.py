from collections import namedtuple
Student = namedtuple('Student',['name','age','DOB'],)
S=Student('Rajesh',29,20112020)
print(S[1])
print(S.name)
print (getattr(S,'DOB')) 
