def max_sum(a):
    total=mylist[0]
    curr=mylist[0]
    for i in range(1,len(a)):
        curr=max(a[1],curr+a[i])
        total=max(total,curr)
    return total
mylist=[4,56,7,8]   
print(max_sum(mylist))    