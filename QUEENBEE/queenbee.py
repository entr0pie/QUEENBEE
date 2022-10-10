#!/bin/python3

import sys

from colorama import Fore, Style

from functions.create import CreateExercise
from functions.search import BeeSearch
from functions.get import GetExercise
from functions.help import help_text

try:
    MODE = sys.argv[1].strip().lower()

except IndexError: 
    help_text()
    sys.exit(1)

if MODE == "-c" or MODE == "--create":
   CreateExercise(None)

if MODE == "-s" or MODE == "--search":
    args = sys.argv[2]
    if "--link" in args: 
        s = BeeSearch(sys.argv[3])
        s.link_search()

    else:
        s = BeeSearch(sys.argv[2])
        s.id_search()

if MODE == "-g" or MODE == "--get":
    script = sys.argv[2]
    
    if len(sys.argv) > 3:
        options = sys.argv[3].strip().lower()
        
        if options == "-o" or options == "--out":
            s = GetExercise(script, sys.argv[4])
            s.get()
            sys.exit(0)
        
    s = GetExercise(script)
    s.get()
