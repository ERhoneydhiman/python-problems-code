
array = []

N = int(input("enter number of element: "))

print("Enter elements of the array :")

for i in range (N):
    user_input = input("Enter an element: ")
    array.append(int(user_input))

dct = {}

for element in array:
    if element in dct:
        dct[element] +=1
        
    else:
        dct[element] = 1
        
for j in dct:
    if dct[j] % 2 == 0:
        print(j, end=" ")
