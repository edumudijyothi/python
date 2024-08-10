def print_numbers(n):
  print(n)#print the current number
  print_numbers(n+1)#recursion calls to next function
  if n>10:
    return      #base case:stop when n is greater than 10
print_numbers(1)
#1-999


