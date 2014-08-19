__author__ = 'Umair'

import string

# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a'
# following 'z'.

def shift(letter):
    all_letters = string.ascii_lowercase
    loc = all_letters.index(letter)
    if loc < all_letters.__len__() - 1:
        return all_letters[loc + 1]
    else:
        return all_letters[0]

        #return all_letters[0]


print(shift('a'))
#>>> b
print(shift('n'))
#>>> o
print(shift('z'))
#>>> a