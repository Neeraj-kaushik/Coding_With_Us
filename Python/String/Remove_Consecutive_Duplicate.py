from collections import OrderdDict

def removeDupWithOrder(str): 
    return "".join(OrderedDict.fromkeys(str))

str=input()
print(removeDupWithOrder)
