n=int(input())
wine=[]
dp=[0]*10001    #첫 번째 잔부터 i번째 잔까지 마셨을 때의 최대 포도주의 양
#i번째 잔을 마시지 않는 경우: 최대 양은 dp[i-1]
#i번째 잔을 마시고, i-1번째 잔은 마시지 않은 경우: 최대 양은 dp[i-2]+wine[i]
#i번째 잔을 마시고, i-1번째 잔도 마시는 경우: 최대 양은 dp[i-3] + wine[i-1] + wine[i]
for i in range(n):
    amount=int(input())
    wine.append(amount)

dp[0]=wine[0]
dp[1]=wine[0]+wine[1]
dp[2]=max(wine[0]+wine[2],wine[1]+wine[2],dp[1])
for i in range(3,n):
    dp[i]=max(dp[i-1],wine[i]+dp[i-2],wine[i]+wine[i-1]+dp[i-3])

print(dp[n-1])

