__author__ = 'Umair'

import string

# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    all_letters = string.ascii_lowercase
    length = all_letters.__len__()
    loc = all_letters.index(letter)
    if loc <= length - 1:
        if loc + n < length:
            return all_letters[loc + n]
        else:
            x = length - loc
            y = n - x
            return all_letters[y]
    else:
        return all_letters[0]


print(shift_n_letters('s', 1))
#>>> t
print(shift_n_letters('s', 2))
#>>> u
print(shift_n_letters('s', 10))
#>>> c
print(shift_n_letters('s', -10))
#>>> i
print(shift_n_letters('z', 26))