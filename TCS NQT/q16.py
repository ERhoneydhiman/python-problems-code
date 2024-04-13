# extract the number from the string , do not choose number which contain 9

my_str = input()

# split string
str_list = my_str.split()

# this array contain only integers
digits_only = [] 

# this is for extract ints from string and put in diffrent array
for char in str_list:
    if char.isdigit():
        digits_only.append(char)


# this check array of ints's string contain any string which contain 9
for i in digits_only:
          if '9' in i:
               digits_only.remove(i)

# this convert str to int
for i in range(len(digits_only)):
    digits_only[i] = int(digits_only[i])

# this find max number from left array
max = digits_only[0]
for i in range(len(digits_only)):
     if digits_only[i] >= max:
          max = digits_only[i]

# print max number from the string doesn't contain 9
print(max)
