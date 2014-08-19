__author__ = 'Umair'

#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    prev_fib = 0
    current_fib = 1
    num = n
    while (num):
        if num == n:
            num -= 1
        else:
            fib = prev_fib + current_fib
            prev_fib = current_fib
            current_fib = fib
            num -= 1
    return fib


print(fibonacci(36))
#>>> 14930352