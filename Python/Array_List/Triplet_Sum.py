def triplet_sum(li,num):
    count=0
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            for k in range(j+1,len(li)):
                if li[i]+li[j]+li[k]==num:
                    count=count+1
    print(count)


t= int(input())
while t>0:
    n=int(input())
    li=[int(x) for x in input().split()]
    num=int(input())
    triplet_sum(li,num)
    t=t-1
