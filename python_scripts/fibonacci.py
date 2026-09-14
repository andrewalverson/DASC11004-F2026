#!/usr/bin/env python3

import argparse

### get the command line arguments ###

# create an argument parser object
parser = argparse.ArgumentParser(description = "This script calculates the Fibonacci number \
                                 for a desired position in the sequence")

# add a required argument – required arguments are called "positional arguments"
parser.add_argument("position", help = "position in the Fibonacci sequence", type=int)

# parse the arguments, store the parsed arguments in a variable called "args"
args = parser.parse_args()

# this is depracated – getting the position from the command line now
# user will enter what position they want the fibonacci number for 
# get the user input
# position = input("Enter the position in the Fibonacci sequence: ")

# calculate the fibonacci number
# initiate our variables for the fibonacci sequence
a,b = 0,1

# loop to calculate the fib number
for i in range(int(args.position)-1):
    a,b = b,a+b

fibonacci_number = a

# print the output
print(f"The Fibonacci number for position {args.position} in the Fibonacci sequences is {fibonacci_number}.")
print(f"The Golden Ratio at this position is {(b/a):.4f}.")
