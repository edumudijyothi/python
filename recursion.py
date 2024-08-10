#recursive n numeric grammimg
def print_numbers(n):
  print(n)#enter th current number
  print_numbers(n+1)
  if n>10:
    return      #base case:stop when n is greater than 10
print_numbers(1)
