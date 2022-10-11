import sys

from colorama import Fore, Style

from functions.beecolors import Colors

C = Colors()

class CommandHandler:
    def __init__(self, command, args):
        self.cmd = command
        self.args = args

class SearchHandler (CommandHandler):
    """ DEFAULT SEARCH CONFIGURATION """

    def gen_config(self):
        query = self.verify_complement(self.cmd)
        output = None

        """ OUTPUT """
        for param in self.args:
            if param in ["-o", "--output"]:
                output = self.verify_complement(param)

        if query == False or output == False:
            self.invalid_complement()

        return {"query":query, "output": output}
        
    
    def verify_complement(self, cmd):
        i = self.args.index(cmd)

        try:
            complement = self.args[i + 1]
            return complement

        except IndexError: 
            return False

    def invalid_complement(self):
        print(f"{C.error} ERROR: parameter evoked without content")
        sys.exit()
    

class RegisterHandler (CommandHandler):
    def gen_config(self):
        i = self.args.index(self.cmd)

        try:
            filePath = self.args[i + 1]
        
        except IndexError:
            print(f"{C.error} ERROR: PATH NOT FOUND")
            sys.exit(1)

        return {"path":filePath}






