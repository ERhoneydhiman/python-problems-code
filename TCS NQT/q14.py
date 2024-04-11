# check given number is a blood related number 
# blood related : if sum of number's digit's factorial = original number

def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num-1)

N = input()
sum = 0
for i in N:
    i = int(i)
    sum = sum + fact(i)

if sum == int(N):
    print('yes')
else:
    print('no')