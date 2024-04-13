# given string consist # and * now task is to print 0 if no of # are equale to no of *
# and print negative diffrence if no # of is greater then * otherwise print positive diff

s = '##**#*#*'
count_hash = 0
count_star = 0
for char in s:
    if char == '#':
        count_hash += 1
    elif char == '*':
        count_star += 1
    else:
        continue

diff = count_star - count_hash

print(diff)
