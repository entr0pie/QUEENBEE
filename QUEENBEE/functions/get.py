import sys

import requests

from functions.beecolors import Colors

C = Colors()


class GetExercise:
    def __init__(self, script, output=None):
        self.script = script
        self.number = ""
        self.output = output
        
        for i in range(len(script)):    
            if script[i] == ".":
                break
            else:
                self.number += script[i]
        

    def get(self):
        if self.output is not None:
            print(f"{C.option} OUTPUTTING TO FILE {self.output}")

        print(f"{C.info} SEARCHING FOR {self.script}")
        link = f"https://raw.githubusercontent.com/entr0pie/QUEENBEE/main/QUEENBEE/ex/{self.number}/{self.script}"
        response = requests.get(link)
        
        if response.status_code != 200:
            print(f"{C.error} ERROR ({response.status_code}): COULD NOT FIND {self.script} IN THE OFICIAL REPOSITORY")
            sys.exit(1)

        else:
            print(f"{C.win} FOUND {self.script}\n")
            lines = response.text.splitlines()

            biggestLineLen = 0 
            for l in range(len(lines)):
                if len(lines[l]) > biggestLineLen:
                    biggestLineLen = len(lines[l])

            line = ""
            semiline = ""

            for i in range(0, biggestLineLen):
                line += "="
                semiline += "-"

            print(line)
            
            for l in range(0, 6):
                print(lines[l])

            print(semiline)

            for l in range(6, len(lines)):
                print(lines[l])


            print('\n' + semiline)
            print(line)

            if self.output is not None:
                file = open(self.output, 'w')
                file.write(response.text)

