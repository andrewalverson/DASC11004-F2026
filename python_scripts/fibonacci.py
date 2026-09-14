#!/usr/bin/env python3

# user will enter what position they want the fibonacci number for 
# get the user input
position = input("Enter the position in the Fibonacci sequence: ")

# calculate the fibonacci number
# initiate our variables for the fibonacci sequence
a,b = 0,1

# loop to calculate the fib number
for i in range(int(position)-1):
    a,b = b,a+b

fibonacci_number = a

# print the output
print(f"The Fibonacci number for position {position} in the Fibonacci sequences is {fibonacci_number}.")
print(f"The Golden Ratio at this position is {(b/a):.4f}.")
