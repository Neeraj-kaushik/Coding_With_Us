def removeDupWithOrder(str):
    t=''
    n=str[0]
    for i in range(1,len(str)):
        if n!=str[i]:
            t=t+n
            n=str[i]
    t=t+str[-1]
    return t


str=input()
print(removeDupWithOrder(str))
