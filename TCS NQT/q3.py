# chocolate question

array = []

N = int(input("enter number of element: "))

print("Enter elements of the array :")

for i in range (N):
    user_input = input("Enter an element: ")
    array.append(int(user_input))
    
    
array_filled = []
array_empty = []

for i in range(len(array)):
    if array[i] != 0:
        array_filled.append(array[i])
    else:
        array_empty.append(array[i])
        
array_filled.extend(array_empty)

for i in range(len(array_filled)):
    print(array_filled[i], end=" ")