#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

DEST_DIR = 'output'

subjects = {}

# Read in file
with open('input.csv', 'r') as f:
    # read each line
    for line in f:
        # split line into list
        split = line.split(',')
        s = split[0]
        r = split[1]
        if s not in subjects:
            subjects[s] = {}
        if r not in subjects[s]:
            subjects[s][r] = []
        
        # Add line to subjects line
        subjects[s][r].append(line)
        

# print(len(subjects['k102NIb']['1']))


# Make output directory
if not os.path.exists(DEST_DIR):
    os.makedirs(DEST_DIR)

# Write out files, following this directory structure:
# k103HZb
# └── bold
#    ├── 024 (maps to run_number 1)
#    ├── 026 (maps to run_number 2)
#    └── 028 (maps to run_number 3)
def map_run_number(run_number):
    if run_number == '1':
        return '024'
    elif run_number == '2':
        return '026'
    elif run_number == '3':
        return '028'


for s in subjects:
    # Make subject directory
    if not os.path.exists(os.path.join(DEST_DIR, s)):
        os.makedirs(os.path.join(DEST_DIR, s))
    for r in subjects[s]:
        # Make run directory
        if not os.path.exists(os.path.join(DEST_DIR, s, 'bold', map_run_number(r))):
            os.makedirs(os.path.join(DEST_DIR, s, 'bold', map_run_number(r)))
        # Write out file
        with open(os.path.join(DEST_DIR, s, 'bold', map_run_number(r), 'selfrel.par'), 'w') as f:
            for line in subjects[s][r]:
                split = line.split(',')
                f.write(','.join(split[2:]))