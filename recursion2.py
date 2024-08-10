def print_numbers(n):
  if n>10:#base case:stop when n is greater than 10
    return 
  print(n)#print the current number
  print_numbers(n+1)#recursion calls to next function
print_numbers(1)
#output:1-10
