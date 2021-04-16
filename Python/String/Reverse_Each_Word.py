str=input()
li=str.split(' ')
t=''
for i in range(len(li)):
    j=li[i]
    t=t+j[::-1]+" "
print(t)