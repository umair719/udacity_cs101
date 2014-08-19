__author__ = 'Umair'
###############################################
#       Exercise by Websten from forums       #
###############################################
# A palindrome is a word or a phrase that reads
# the same backwards as forwards. Make a program
# that checks if a word is a palindrome.
# If the word is a palindrome, print 0 to the terminal,
# -1 otherwise.
# The word contains lowercase letters a-z and
# will be at least one character long.
#
### HINT! ###
# You can read a string backwards with the following syntax:
# string[::-1] - where the "-1" means one step back.
# This exercise can be solved with only unit 1 knowledge
# (no loops or conditions)

word = "madam"
# test case 2
word = "madman"  # uncomment this to test

###
# YOUR CODE HERE. DO NOT DELETE THIS LINE OR ADD A word DEFINITION BELOW IT.
###ca

is_palindrome = 0 if (word[::-1] == word) else -1

# TESTING
print(is_palindrome)
# >>> 0  # outcome if word == "madam"
# >>> -1 # outcome if word == "madman"

cost = 0
items = [1, 10]
for x in items:
    tax = x * 0.08
    tip = x * 0.18
    cost = cost + x + tax + tip
print(cost)

n = 10
while n > 1:
    print(n)
    if n % 2 == 0:
        n = n / 2
    else:
        n = 3 * n + 1
