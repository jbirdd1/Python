# Name: Jessica Morton
# Evergreen Login: morjes14
# Computer Science Foundations
# Programming as a Way of Life
# Lab 3


n = 10
series = 'fibonacci'

if series == 'fibonacci':
    x = 0
    y = 1
    for i in range(n-1):
        fib = x + y
        x = y 
        y = fib
        print fib

if series == 'sum':
    total = 0
    x = 1
    for i in range(n):
        total = total + (3*x)
        x = x + 1
        print total