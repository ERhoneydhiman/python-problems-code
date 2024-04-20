arr = [1,2,2,6]
freq = {}
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for i in range(len(arr)):
    arr[i] = freq[arr[i]]

print(arr)