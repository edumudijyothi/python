num=23451
total_sum=0
while num>0:
  total_sum+=num%10
  num//=10#return the last value

print(total_sum) 
""""Explanation (step by step):

Start: num = 23451, total_sum = 0

Iteration 1
num % 10 = 1 (last digit)
total_sum = 0 + 1 = 1
num //= 10 → 2345

Iteration 2
num % 10 = 5
total_sum = 1 + 5 = 6
num //= 10 → 234

Iteration 3
num % 10 = 4
total_sum = 6 + 4 = 10
num //= 10 → 23

Iteration 4
num % 10 = 3

total_sum = 10 + 3 = 13
num //= 10 → 2
Iteration 5
num % 10 = 2

total_sum = 13 + 2 = 15
num //= 10 → 0 (loop ends)
✅ Final Result:
total_sum = 15
"""
