s = input("enter string: ")
p = int(input('enter value of p: '))
temp =[]
dct = {}
for i in s:
    if i not in dct:
        dct[i] = 1
    else:
        dct[i] +=1
        
for key in dct:
    if dct[key] >= p:
        temp.append(key)

temp.sort()
        
print(temp[0])
