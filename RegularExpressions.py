#Function compile() Regular expressions are compiled into pattern objects, which have methods for various operations such as searching for pattern matches or performing string substitutions. 
import re
p=re.compile('[a-e]')
print(p.findall("Hi Rajesh You are rocking "))
p1=re.compile('\d')
print(p1.findall("i born at 7 am 10 march 1992"))
p1=re.compile('\d+')
print(p1.findall("i born at 7 am 10 march 1992"))
#\w s equivalent to [a-zA-Z0-9_]
p2=re.compile('\w')
print(p2.findall('hi rajesh how are you '))
# \w+ matches to group of alphanumeric character. 
p3=re.compile('\w+')
print(p3.findall('hi rajesh how are you '))
# \W matches to non alphanumeric characters. 
p4 = re.compile('\W') 
print(p4.findall("he said *** in some_language.")) 
print(re.sub('ub','~*',"Subject has Uber booked already", flags=re.IGNORECASE))
