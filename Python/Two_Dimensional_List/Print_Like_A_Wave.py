def Print_Like_Wave(li,n,m):
    for j in range(m):
        for ele in li:
            if j%2==0:
                print(ele[j],end=' ')
            else:
                
                          

t=int(input())
while t>0:
    str=input().split()
    n,m=int(str[0]),int(str[1])
    li=[[int(j) for j in input().split()] for i in range(n)]
    Print_Like_Wave(li,n,m)
    t=t-1