n=int(input())
li=[int(x) for x in input().split()]
ele=int(input())
isfound=False
for i in range(len(li)):
    if li[i]==ele:
        print(i)
        isfound=True
        break
if isfound is False:
    print(-1)