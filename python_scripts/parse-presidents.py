#! /usr/bin/env python3

from collections import defaultdict # we use this to avoid KeyErrors

# make some dictionaries
presidents = defaultdict(str) # key = president num, value = president name
wikis      = defaultdict(str) # key = president number, value = wikipedia page
parties    = defaultdict(int) # key = party name, value = party count

# define our input file
input_file = '../data/presidents.csv'

with open(input_file, 'r') as prez_file:
    # loop over the file line-by-line
    for line in prez_file:
        # split each line at the comma to create a list called 'columns'
        columns = line.split(',')

        # could do this if wanted to
        prez_num = columns[0]

        # loading our dictionaries
        presidents[columns[0]] = columns[1]
        wikis[columns[0]] = columns[2]
        parties[columns[5].strip()] += 1


"""
# get stuff from our dictionary
# index one entry
print(presidents.get('16'))
print(presidents['16'])
print(presidents.get('48', "Not elected yet, we're only at 47"))

# loop over dictionary
for num in presidents.keys():
    print(f'president number {num} was {presidents.get(num)}')


# another way to loop over a dictionary
for number, page in wikis.items():
    print(f"the page for president number {number} ({presidents[number]}): {page}")
"""

# loop over the party count dictionary
for whatever in parties.keys():
    print(f"{whatever}: {parties[whatever]}")


    