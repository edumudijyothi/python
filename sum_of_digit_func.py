def sum_of_digits(n):
    #base case:if n is 0, the sum is0
    if n==0:
        return 0
    
    else:
        return n%10+sum_of_digits(n//10)
n=int(input())
print(sum_of_digits(n))    
   #input:8908
   #25 