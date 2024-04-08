a = [[0,1,0,0,1],
    [1,1,0,1,1],
    [0,0,0,0,1],
     [0,0,0,0,1],
    [1,0,1,1,0]]


n = 0
p = 0

for i in range(len(a)):
    m = 0
    for j in range(len(a[i])):
        if(a[i][j]==1):
            m+=1
    if(m > n):
        n = m
        p = i+1

print(p, " raw has max cars that is " , n)