#Dictionary Python
Dict={'Rajesh':28,'Python':3,'Divya':28}
print(Dict['Rajesh'])
print(Dict)
Dict.update({"Python":90})
print(Dict)
del Dict['Python']
print(Dict)
Dict.update({"Abhi":29})
print("Employee Name: %s" % list(Dict.items()))
# checking the list values

Dict1={'Rajesh':29,'Abhimanyu':39,'Rohit':34,'Sam':35}
Men={'Rajesh':29,'Abhimanyu':39,'Rohit':34}
Women={'Sam':35}
for key in Dict1.keys():
    if key in Men.keys():
        print(True)
    else:
        print(False)
print("Sorting the Dictionary Keys: \n")
Students =list(Dict1.keys())
print(Students)
Students.sort()
print(Students)
#sorting
for s in Students:
    print(":".join((s,str(Dict1[s]))))

print("Length of the Dictionary %d:" % len(Dict1))
# variable types
print("Variable types : %s" %type(Dict1))

#Dictionary into printable String format
print("Printable String : %s" % str(Dict1))
#merging
#Dict1.update(Dict)
myDict={**Dict,**Dict1}
print(myDict)
print("Rajesh" in myDict)
print(len(myDict))
myDict.pop("Rajesh")
print(len(myDict))