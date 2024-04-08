S = input("enter string: ")

vowel ='AEIOUaeiou'
special = '!@#$%^&*?<>|/\=+-_`~'
nums = '1234567890'

V = 0
SP = 0
N = 0
c = 0
for i in S:
    if i in vowel:
        V+=1
    elif i in special:
        SP+=1
    elif i in nums:
        N+=1
    else:
        c+=1
        
print("vowel are", V, ", special chars are ", SP, 'numbers are ', N , '& consonent are ', c)
        