__author__ = 'Umair'

# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

def is_palindrome(s):
    length = s.__len__()
    if length > 0:
        if s[0] == s[length - 1]:
            leftover = s[1:-1]
            if is_palindrome(leftover):
                return True
            else:
                return False
        else:
            return False
    else:
        return True


#print(is_palindrome(''))
#>>> True
#print(is_palindrome('abab'))
#>>> False
#print(is_palindrome('abba'))
#>>> True
print(is_palindrome('andrea'))
#>>> False