#!/usr/bin/env/ python

def fib(upper):
    # write Fibonacci series up to upper
    a, b = 0, 1
    while b < upper:
        print(b)
        new_a = b
        b = a+b
        a = new_a # We need to do this update after updating b, because there, we need to use a's old value
    return

print(fib(2000))