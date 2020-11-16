from collections import Counter
list1 = ['x','y','z','x','x','x','y', 'z']
print(Counter(list1))
myStr="i am rajesh learning pythong "
print(Counter(myStr))
#counter with tuple
dict1 =  {'x': 4, 'y': 2, 'z': 2, 'z': 2}
print(Counter(dict1))
#sleep
import time

print('Code Execution Started')

def display():
    print('Welcome to Guru99 Tutorials')
    time.sleep(5)

display()
print('Function Execution Delayed')