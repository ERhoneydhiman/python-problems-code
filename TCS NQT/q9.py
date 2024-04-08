N = int(input('enter year: '))
temp = N // 100 
rem = N % 100

if rem == 0:
    print(temp)
else:
    print(temp + 1)
    
# done