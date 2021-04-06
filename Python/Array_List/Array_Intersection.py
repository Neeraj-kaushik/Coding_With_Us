def array_intersection(n,li,m,li1):
    for i in range(len(li)):
        for j in range(len(li1)):
            if li[i]==li1[j]:
                print(li[i], end=" ")
                break


t=int(input())
while t>0:
    n=int(input())
    li=[int(x) for x in input().split()]
    m=int(input())
    li1=[int(a) for a in input().split()]
    array_intersection(n,li,m,li1)
    t=t-1
