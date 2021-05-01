s=input()
words=s.split()
d={}
for w in words:
    if w in d:
        d[w]=d[w]+1
    else:
        d[w]=1
print(d)