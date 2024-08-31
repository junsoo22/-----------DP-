n=int(input())
dp=[5000]*5001

dp[3]=dp[5]=1

for i in range(6,n+1):
    dp[i]=min(dp[i-3],dp[i-5])+1
    

if dp[n]<5000:
    print(dp[n])
else:
    print(-1)