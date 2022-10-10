#!/bin/python3

import sys

from colorama import Fore, Style

from functions.create import CreateExercise
from functions.search import BeeSearch

def help_text():
    text = f"{Fore.YELLOW}" + """    
                                                    >=>                          
                                                    >=>                          
      >=>    >=>  >=>   >==>      >==>    >==>>==>  >=>        >==>      >==>    
    >>  >=>  >=>  >=> >>   >=>  >>   >=>   >=>  >=> >=>>==>  >>   >=>  >>   >=>  
    >>  >=>  >=>  >=> >>===>>=> >>===>>=>  >=>  >=> >=>  >=> >>===>>=> >>===>>=> 
     >==>=>  >=>  >=> >>        >>         >=>  >=> >=>  >=> >>        >>        
        >=>    >==>=>  >====>    >====>   >==>  >=> >=>>==>   >====>    >====>   
        >==>                                                                     
    \n\n""" + f"{Style.RESET_ALL}"
    text += "USAGE: python3 queenbee.py [MODE] [OPTIONS]\n\n"
    text += "   MODES:\n"
    text += "     -c | --create         Register a new solution.\n"
    text += "     -s | --search         Search for an specific exercise\n"
    text += "                             (ex: python3 queenbee.py -s 1084)\n"
    # text += "\n"
    text += "   OPTIONS:\n"
    text += "   [SEARCH SECTION]\n"
    text += "     --link                Do the search by a beecrowd link.\n"


    print(text)

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
