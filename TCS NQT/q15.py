#  check comman string in both string

st1 = 'look'
st2 = 'book'
set1 = set(st1)
set2 = set(st2)
ans = ''
for i in set1:
    if i in st2:
        ans = ans + i

print(ans)