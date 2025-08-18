#formal input, argument inpur ,
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4)) 


#without factorial
def fact(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
print(fact(4))    '''4! = 4 x 3 × 2 × 1=24'''
