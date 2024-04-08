array = [0,1,2,3,2,1,3,0,3,0]

for i in range(len(array)):
    for j in range(len(array)):
        if array[j] > array[i]:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp

array