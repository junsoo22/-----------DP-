d=[0]*1001

def dp(n):
    if n==1:
        return 1
    if n==2:
        return 3
    if d[n]!=0:
        return d[n]
    else:
        d[n]=(dp(n-1)+2*dp(n-2))%10007
        return d[n]
    
n=int(input())
print(dp(n))