n=int(input("Enter the values"))
fibonacci=[0,1]
for i in range(1,n):
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
print(fibonacci)