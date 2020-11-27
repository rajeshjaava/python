def ask_ok(prompt,retries=4,reminder='Please Try Again !'):
    while True:
        ok=input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries=retries-1
        if retries<0:
            raise ValueError('Invalid User Response')
        print(reminder)
ask_ok('Do you really want to quit?')

"""
Response:

PS F:\workspace\Python\python> python Functions.py
Do you really want to quit?8
Please Try Again !
Do you really want to quit?-1
Please Try Again !
Do you really want to quit?0
Please Try Again !
Do you really want to quit?9
Please Try Again !
Do you really want to quit?8
Traceback (most recent call last):
  File "F:\workspace\Python\python\Functions.py", line 12, in <module>
    ask_ok('Do you really want to quit?')
  File "F:\workspace\Python\python\Functions.py", line 10, in ask_ok
    raise ValueError('Invalid User Response')
ValueError: Invalid User Response
PS F:\workspace\Python\python> 
"""