n=45
count=0
i=1
while(i<n):#it takes n divisible numbers works & time complexity way
    if n%i==0:
        count=count+1
    i+=1
if count==1:
    print("prime")
else:
    print("not prime")
        