t=int(input())


for i in range(t):
    dp=[]
    k=int(input())   #1층
    n=int(input())   #3호
    for j in range(1,n+1):
        dp.append(j)
    for k in range(k):
        for l in range(1,n):
            dp[l]+=dp[l-1]
    print(dp[-1])



#1층 3호에 사려면
# 0층의 1호부터 3호까지 사람들의 수의 합만큼 살아야함
#0층의 1호:1명, 2호:2명, 3호:3명

#2층 3호에 사려면
#1층의 1호부터 3호까지 사람들의 수
#1층 1호:1, 1층 2호:3, 1층 3호:6명
#2층 1호:1, 2층 2호:1+3=4, 2층 3호:4+6=10
#3층 1호:1, 3층 2호:1+4=5, 3층 3호:5+10=15