def check_permuntation(str1,str2):
    length1=len(str1)
    length2=len(str2)
    if length1==length2:
        for i in range(len(str1)):
            if str1[i] in str2:
                return True
            else:
                return False
    else:
        return False        

str1=str(input())
str2=str(input())
ans=check_permuntation(str1,str2)
if ans is True:
    print('true')
else:
    print('false')