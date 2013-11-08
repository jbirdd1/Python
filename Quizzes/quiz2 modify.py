# Name: Jessica Morton
# Evergreen Login: morjes14
# Computer Science Foundations
# Programming as a Way of Life
# Lab 3

n = 10
series = 'fibonacci'

def fib(n):
    x = 0
    y = 1
    for i in range(n-1):
        fib = x + y
        x = y 
        y = fib
        print fib
    return fib
    
def sum(n):
    total = 0
    x = 1
    for i in range(n):
        total = total + (3*x)
        x = x + 1
        print total
    return total

if series =='fibonacci':
    fibResult = fib(n)
    print fibResult
    
if series == 'sum':
    sumResult = sum(n)
    print sumResult