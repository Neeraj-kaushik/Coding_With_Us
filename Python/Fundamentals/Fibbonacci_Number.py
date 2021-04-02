num=int(input())
value1=0
value2=1
i=1
while i<num:
    fabno=value1+value2
    value1=value2
    value2=fabno
    i=i+1
print(fabno)