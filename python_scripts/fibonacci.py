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

    # add an optional argument for verbose or simple output
    # if 'store_true', this means assign 'True' if the argument is specified
    # on the command line: this means that the default for 'store_true' is false
    parser.add_argument("-v", "--verbose", help = "print verbose output or not (default is non-verbose)", action='store_true')

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
    golden_ratio = b/a
    return fibonacci_number, golden_ratio


####---- function to print the output
def print_output(pos, fib_num, golden_ratio):

    # if verbose
    if args.verbose:
        print(f"The Fibonacci number for position {pos} in the Fibonacci sequences is {fib_num}.")
        print(f"The Golden Ratio at this position is {golden_ratio:.4f}.")

    # else not verbose
    else:
        print(','.join([str(pos), str(fib_num), str(golden_ratio)]))

####---- main() function
def main():
    # call the function to calculate the fibonacci number
    # the real business happens here
    fib, golden_ratio = calc_fib(args.position)

    # print the output
    print_output(args.position, fib, golden_ratio)

# command-line parsing happens in the outermost (global) level of the script
args = get_input()

# set the environment for this script
# is it a standalone script with main()? 
# or is this a module being called by another script?
if __name__ == '__main__':
    main()
