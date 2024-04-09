# Que : check number is devided by 3 or not

N = input()
# N = int(N)

# if N % 3 == 0:
#     print('yes')
# else:
#     print('no')

# another method

sum = 0
for i in N:
    i = int(i)
    sum += i

if sum % 3 == 0:
    print('yes')
else:
    print('no')