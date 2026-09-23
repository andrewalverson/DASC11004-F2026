#!/usr/bin/env python3

import argparse


####---- function to get command-line arguments

### get the command line arguments ###
def get_input():
    # create an argument parser object
    parser = argparse.ArgumentParser(description = "This script calculates the Fibonacci number \
                                    for a desired position in the sequence")

    # add a required argument – required arguments are called "positional arguments"
    parser.add_argument("position", help = "position in the Fibonacci sequence", type=int)

    # parse the arguments, store the parsed arguments in a variable called "args"
    return parser.parse_args()


####---- function to calculate the fibonacci number
def calc_fib(n):
    # calculate the fibonacci number
    # initiate our variables for the fibonacci sequence
    a,b = 0,1

    # loop to calculate the fib number
    for i in range(n-1):
        a,b = b,a+b

    fibonacci_number = a
    return fibonacci_number

####---- function to print the output
def print_output(p,f):
    # print the output
    print(f"The Fibonacci number for position {p} in the Fibonacci sequences is {f}.")
    #print(f"The Golden Ratio at this position is {(b/a):.4f}.")



####---- main() function
def main():
    # call the function to calculate the fibonacci number
    # the real business happens here
    fib = calc_fib(args.position)

    # print the output
    print_output(args.position, fib)


# command-line parsing happens in the outermost (global) level of the script
args = get_input()

# set the environment for this script
# is it a standalone script with main()? 
# or is this a module being called by another script?
if __name__ == '__main__':
    main()
