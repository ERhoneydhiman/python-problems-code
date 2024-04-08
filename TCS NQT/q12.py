# Que: Given string sort the string on the basis of that given key string that is given like s = 'apple' key = 'eapl' sort s on basis of key so answer is eappl

s = input()
key = input()
s_dict = {}
ans = ''
for i in s:
    if i not in s_dict:
        s_dict[i] = 1
    else:
        s_dict[i] += 1 

for i in key:
    if i in s_dict:
        temp = i*s_dict[i]
        ans += temp
        del s_dict[i]




print(ans)
