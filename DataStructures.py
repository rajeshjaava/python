#Tuples
import numbers

tup1=('Robert','Rajesh',"AbhiRam",10,1992);
tup2=(1,2,3,4,5,6,7,8);
print(tup1[0])
print(tup2[0:4])

#packaging
x=("Rajesh",29,"Learning Python",2020)
print(x)
(name,age,course,year)=x
print(name)
print(year)

#directory[last,first]=number
a={'x':100,'y':200}
b=list(a.items())
print(b)
#Slicing of Tuple
x = ("a", "b","c", "d", "e")
print(x[2:4])
