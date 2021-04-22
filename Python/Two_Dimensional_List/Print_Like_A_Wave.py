def Print_Like_Wave(li,n,m):
    for i in range(n):
        for j in range(m):
            if j%2==0:
                print(li[j][i],end=' ')
        
                          

t=int(input())
while t>0:
    str=input().split()
    n,m=int(str[0]),int(str[1])
    li=[[int(j) for j in input().split()] for i in range(n)]
    Print_Like_Wave(li,n,m)
    t=t-1