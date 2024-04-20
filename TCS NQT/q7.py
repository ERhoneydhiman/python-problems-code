m  = [[1,2,3]
      ,[4,5,6]
      ,[7,8,9]]
b = []
for i in range(len(m)):
    for j in range(len(m[i])):
#         print(i,j)
        m[i][j] = m[j][i]