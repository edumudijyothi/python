N=int(input())
Desired=list(map(int,input().split()))
actual=list(map(int,input().split()))
minimum_loss=0
for i in range(N):
    minimum_loss+=abs(Desired[i]-actual[i])
print(minimum_loss)    #something wrong