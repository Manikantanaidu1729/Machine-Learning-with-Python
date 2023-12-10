list1=[5,7,4,7,4,6,4,53,4,4]
tuple=((2,10),(1,5),(6,8))
dict1={3:"e",2:"a",1:"c",7:"b",5:"d"}

print(sorted(list1))
print(sorted(list1,reverse=True))
print(sorted(tuple))

print(sorted(dict1))
print(sorted(dict1.keys()))
print(sorted(dict1.values()))
print(sorted(dict1.items()))
print(sorted(dict1.items(),key=lambda x:x[1]))

def secondvalue(element):
    return element[1]

print(sorted(tuple,key=secondvalue))