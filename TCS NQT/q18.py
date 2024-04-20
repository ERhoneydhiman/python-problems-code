b = ['w', 'r', 'y', 'w', 'g', 'r', 'y', 'y']
temp = []
b_dict = {}

for i in b:
    if i in b_dict:
        b_dict[i] += 1

    else:
        b_dict[i] = 1
for i in b_dict:
    if b_dict[i] % 2 != 0:
        temp.append(i)

print(temp[0])