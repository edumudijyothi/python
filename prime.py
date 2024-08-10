n=45
a=int(n/2)#it takes of(n/2) divisible numbers works & time reduce way
count=0
i=1
while(i<a):
    if n%i==0:
        count=count+1
    i+=1
if count==1:
    print("prime")
else:
    print("not prime")
    #this is time optimize way
        