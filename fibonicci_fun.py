def fibonacci(n):#base case:return n if 0 or 1
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))#function calling    
#in recursion else statement works intenally    