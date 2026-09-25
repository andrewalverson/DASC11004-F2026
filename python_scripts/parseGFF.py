#!/usr/bin/env python3

import argparse
import csv

# read in the genome and store it in a variable
# genome sequence will be held in 'genome_sequence'
genome_sequence = ''

# read in the GFF file
with open(gff_file, 'r') as gff:
    # create a csv reader object called 'reader', delimter = '\t'

    for line in reader:
        # get start and end positions
        start = line[3]
        end   = line[4]
        attributes = line[8]

        feature_sequence = genome_sequence[start:end] # <- check these number (add 1 or subtract 1)

        print(">" + attributes)
        print(feature_sequence)