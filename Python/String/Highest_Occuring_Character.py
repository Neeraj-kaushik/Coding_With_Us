str=input()
var1=sorted(str)
max=-1
print(var1)
for i in range(len(var1)-1):
    for j in range(i+1,len(var1)):
        if var1[i]!=var1[j]:
            s=j-i 
            print(s)
            if max<s:
                max==s
                var2=var1[i]         
            i=j
print(var2)