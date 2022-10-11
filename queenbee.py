#!/bin/python3
import sys
from datetime import datetime

from colorama import Fore, Style

from functions.help import help_text
from functions.search import BeeSearch
from functions.handlers import RegisterHandler, SearchHandler
from functions.register import RegisterExercise

""" DISPLAY HELP """
if len(sys.argv) == 1:
    help_text()
    sys.exit(1)

time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"{Fore.YELLOW}STARTING QUEENBEE v1{Style.RESET_ALL} AT [{Fore.CYAN}{time}{Style.RESET_ALL}]", end=" ")

""" SEARCH SECTION """
search = ["-s", "--search"]

for cmd in search:
    if cmd in sys.argv:
        print(f"({Fore.MAGENTA}SEARCH MODE{Style.RESET_ALL})")
        handler = SearchHandler(cmd, sys.argv)
        settings = handler.gen_config()
        bee = BeeSearch(settings["query"], settings["output"])
        bee.search()


""" REGISTER SECTION """

register = ["-r", "--register"]
for cmd in register:
    if cmd in sys.argv:
        print(f"({Fore.MAGENTA}REGISTER MODE{Style.RESET_ALL})")
        handler = RegisterHandler(cmd, sys.argv)
        settings = handler.gen_config()
        RegisterExercise(settings["path"])