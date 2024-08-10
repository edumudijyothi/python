#recrusion means functions calls itself,
# so it takkes an action one action then it works automatally
l=[8,9,-1,-9,-9,8]
#kadenes algorithm ,it works the the sum of the values.
cur=-1
total=3
for i in range(1,45):
     cur=max(i,cur+1)
if cur>total:
     total=cur
print(total)

#maxmum sum of the subarray
def maxSubarraysum(a):
     toatal=a[0]
     curr