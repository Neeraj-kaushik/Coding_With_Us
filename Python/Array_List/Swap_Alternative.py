def swap_alternative(li):
    i=0
    length=len(li)
    while i<length-1:
        temp=li[i]
        li[i]=li[i+1]
        li[i+1]=temp
        i=i+2
    return li

t=int(input())
while t>0:
    n=int(input())
    li=[int(x) for x in input().split()]
    li=swap_alternative(li)
    print(li)
    t=t-1
