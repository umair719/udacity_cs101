__author__ = 'Umair'

import string

# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def rotate(input, n):
    all_letters = string.ascii_lowercase
    length = all_letters.__len__()
    return_string = ""
    for letter in input:
        if letter == ' ':
            return_string += letter
        else:
            loc = all_letters.index(letter)
            if loc <= length - 1:
                if loc + n < length:
                    return_string += all_letters[loc + n]
                else:
                    x = length - loc
                    y = n - x
                    return_string += all_letters[y]
            else:
                return_string += all_letters[0]
    return return_string


print(rotate('sarah', 13))
##>>> 'fnenu'
print(rotate('fnenu', 13))
###>>> 'sarah'
print(rotate('dave', 5))
###>>>'ifaj'
print(rotate('ifaj', -5))
###>>>'dave'
print(rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu sv rscv kf ivru kyzj"), -17))
#>>> ???