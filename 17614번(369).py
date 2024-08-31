# n=int(input())

# count=0
# for i in range(1,n+1):
#     for j in str(i):
#         if j=='3'or j=='6' or j=='9':
#             count+=1
# print(count)


#21965번

# n=int(input())

# arr=list(map(int,input().split()))
# check=True
# shape=True
# for i in range(n-1):
#     if arr[i]<arr[i+1]:
#         if shape==False:
#             check=False
#     elif arr[i]==arr[i+1]:
#         check=False
#         break
#     else:
#         shape=False

# if check:
#     print("YES")
# else:
#     print("NO")

    

#1026번
# n=int(input())
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))

# result=0
# a.sort()

# for i in range(n):
#     bmax=max(b)
#     result+=a[i]*bmax
#     b.remove(bmax)
# print(result)

    

#19941번

