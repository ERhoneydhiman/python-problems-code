N = input('enter N : ')
p = 1
s = 0
for i in N:
    i = int(i)
    p = p * i
    s = s + i
    
diff = p-s

print('price is ', diff)