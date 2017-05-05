#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description = 'Converts char files to python double lists')
parser.add_argument('charfile', help='filename for conversion as an 8x10 ones or zeros map')

args = parser.parse_args()

with open(args.charfile) as the_file:
    lines = the_file.read().split('\n')[:-1]

char_map = map(lambda line: list(line), lines)
print char_map
