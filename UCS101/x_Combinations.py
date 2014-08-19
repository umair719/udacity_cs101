__author__ = 'Umair'


def combinations(max, limit):
    return factorial(max) / (factorial(max - limit) * factorial(limit))


def factorial(num):
    fac = 1
    for x in range(1, num + 1):
        fac *= x
    return fac


def permutations(types, slots):
    return factorial(types) / factorial(types - slots)


#print(combinations(5,3))


#print(factorial(6))

#print(permutations(4,3))

def user_perm():
    cont = 'y'
    while (cont == 'y'):
        print(permutations(int(input("How many unique possibilities: ")), int(input("How many slots: "))))
        cont = input("Continue? [y/n] :")


user_perm()