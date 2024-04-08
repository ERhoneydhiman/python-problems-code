# q4

N = bin(int(input()))  [2:]
x = ""
for i in N:
    if i == '1':
        x += "0" 
    else:
        x += "1"

ans = int(x,2)
print(N)
print(x)
print(ans)

N