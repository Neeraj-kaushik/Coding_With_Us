li=[1,2,1,3,2,3,4,3,54,6,55,4324,23]
s=set()
for i in li:
    s.add(i)
sum=0
for i in s:
    sum=sum+i
print(sum)