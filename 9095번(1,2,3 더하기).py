t=int(input())
dp=[0]*1000


for i in range(t):
    n=int(input())
    dp[1]=1
    dp[2]=2
    dp[3]=4
    for j in range(4,n+1):
        dp[j]=dp[j-3]+dp[j-2]+dp[j-1]
    print(dp[n])
    