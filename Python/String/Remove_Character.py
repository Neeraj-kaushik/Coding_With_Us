str=input()
x=input()
t=''
for i in range(len(str)):
    if x!=str[i]:
        t=t+str[i]
if str[-1]!=x:
    t=t+str[-1]
print(t)