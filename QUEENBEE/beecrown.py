#!/bin/python3

import sys

from functions.create import CreateExercise

try:
    MODE = sys.argv[1].strip().lower()

except IndexError: 
    print("USAGE: python beecrown [MODE] [OPTIONS]")
    sys.exit(1)

if MODE == "-c":
   CreateExercise(None)

