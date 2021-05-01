#ways to create dictionary
a={'the':1,'name':'Neeraj'}
b=a.copy()
c=dict([('the',1),('name','rahul')])
d=dict.fromkeys(['the',2,3,],10)
print(a)
print(b)
print(c)
print(d)
e={1:2,3:4,'list':[1,2], "diction":{1:2}}
print(e.keys())
print(e.values())
print(a.get(1))
print(a.get('li',0))
for i in e:
    print(i)
e['tuple']=(1,2,3,4)
print(e)
e.pop(1)
print(e)