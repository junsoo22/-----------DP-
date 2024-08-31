
t=int(input())
for i in range(t):
    d1=[1,0]
    d2=[0,1]
    n=int(input())
    if n>1:
        for j in range(n-1):
            d1.append(d2[-1])

            d2.append(d1[-2]+d2[-1])
    print(d1[n],d2[n])


        

    
