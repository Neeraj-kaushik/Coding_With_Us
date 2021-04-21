def row_wise_sum(li,n,m):
    sum1=0
    for i in range(n):
        for j in range(m):
            sum1=sum1+li[i][j]
        print(sum1)
        sum1=0

t=int(input())
while t>0:
    str=input().split()
    n,m=int(str[0]),int(str[1])
    li=[[int(j) for j in input().split()] for i in range(n)]
    row_wise_sum(li,n,m)
    t=t-1

