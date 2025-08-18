n=int(input("Enter the values"))
fibonacci=[0,1]
for i in range(1,n):
    fibonacci.append(fibonacci[-1]+fibonacci[-2])

print(fibonacci)

#fastest way of iteration 
def fab_iter(n):
    a,b=0,1
    for _ in range(1,n+1):
        a,b=b,a+b
    return a
print(fab_iter(5)) 
'''Tracing for n=5
Start: (a=0, b=1)
Step 1 → (a=1, b=1)
Step 2 → (a=1, b=2)
Step 3 → (a=2, b=3)
Step 4 → (a=3, b=5)
Step 5 → (a=5, b=8)
After 5 updates → a = 5'''
