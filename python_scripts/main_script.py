#!/usr/bin/env python3

import csv
import cowsay
import argparse
import my_neat_functions

def main():
    user_input_name = input('Enter your name: ')
    my_neat_functions.greeting(user_input_name)

"""
    csv.reader
    argparse.add_argument
    cowsay.char_names
"""

# set the environment for this script
# is it a standalone script with main()? 
# or is this a module being called by another script?
if __name__ == '__main__':
    main()
