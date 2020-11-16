#factorial of the number
def factorial(n):
    return 1 if(n==0 or n==1) else n*factorial(n-1)
#driver class
print(factorial(3))