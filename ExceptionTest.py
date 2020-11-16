import sys
randomList=[1,2,3,5]
for entry in  randomList:
    try:
        print("entry is ", entry)
        r=entry/int(1)
        break
    except Exception as e:
        print("Oops .! ",e.__class__,"occured ")
        print("Next entry")
        print()
print("the reciprocal of ",  entry "is ",r)
