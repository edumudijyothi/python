n=5
start=10
end=50
multiples=[]
for i in range(start,end+1):
    if(i%n==0):
        multiples.append(i)
print("multiples of" ,n, "from", start,"to",end,"are:",multiples)

