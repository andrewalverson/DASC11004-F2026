#!/usr/bin/env python3

import cowsay
import random

####---- function to say hello
def greeting(name):
    print(f'hello, {name}')
    char = random.choice(cowsay.char_names)
    print(f'your animal is', char)
    getattr(cowsay,char)('hello')




    
####---- function to calculate the fibonacci number
def calc_fib(n):
    # calculate the fibonacci number
    # initiate our variables for the fibonacci sequence
    a,b = 0,1

    # loop to calculate the fib number
    for i in range(n-1):
        a,b = b,a+b

    fibonacci_number = a
    golden_ratio = b/a
    return fibonacci_number, golden_ratio


# set the environment for this script
# is it a standalone script with main()? 
# or is this a module being called by another script?
if __name__ == '__main__':
    main()
