def largest_sum(li,n,m):
    max_row=-1
    max_column=-1
    sum1=0
    sum2=0
    for i in range(n):
        for j in range(m):
            sum1+=li[i][j]
        if max_row<sum1:
            max_row=sum1
            row=i
        sum1=0
    for i in range(n):
        for j in range(m):
            sum2+=li[j][i]
        if max_column<sum2:
            max_column=sum2
            column=j
        sum2=0
    if max_row<max_column:
        print('column',j,max_column)
    else:
        print('row',i,max_row)

t=int(input())
while t>0:
    str=input().split()
    n,m=int(str[0]),int(str[1])
    li=[[int(j) for j in input().split()] for i in range(n)]
    largest_sum(li,n,m)
    t=t-1