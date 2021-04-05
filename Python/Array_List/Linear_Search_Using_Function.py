def linear_search(li,ele):
    for i in range(len(li)):
        if li[i]==ele:
            return i
            break
    return -1

n=int(input())
li=[int(x) for x in input().split()]
ele=int(input())
value=linear_search(li,ele)
print(value)