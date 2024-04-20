def isVelid (i,j,m,n):
    if i>=0 and j>=0 and i<m and j<n:
        return True
    else:
        return False


array = [[10, 20, 15],
         [21, 30, 14],
         [7, 16, 32]]

peek_array = []
for i in range(len(array)):
    for j in range(len(array[i])):

        curr = array[i][j]

        left = 0
        right = 0 
        top = 0
        bottom = 0

        if isVelid(i,j-1,len(array), len(array[i])):
            left = array[i][j-1]
        else:
            left = float( '-inf')

        if isVelid(i,j+1,len(array), len(array[i])):
            right = array[i][j+1]
        else:
            right = float( '-inf')

        if isVelid(i-1,j,len(array), len(array[i])):
            top = array[i-1][j]
        else:
            top = float( '-inf')

        if isVelid(i+1,j,len(array), len(array[i])):
            bottom = array[i+1][j]
        else:
            bottom = float( '-inf')

        if curr >= left and curr >= right and curr>=top and curr>=bottom:
            print(array[i][j])