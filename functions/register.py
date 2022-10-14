from datetime import date
from os import system
import json
import sys

import requests

from functions.beecolors import Colors

C = Colors()

class RegisterExercise:
    def __init__(self, path):
        self.path = path
        self.collect_data()
        header = self.create_header()

        system(f"mkdir repo/{self.number}")
        newFile = open(f"repo/{self.number}/{self.number}{self.endfile}", 'x')
        newFile.write(header)
        newFile.write(self.fileContent)
    
    def collect_data(self):
        
        """ SEARCHING LOCAL FILE """

        print(f"{C.warn} OPENING {self.path}")
        
        try:
            self.fileContent = open(self.path, 'r').read()

        except FileNotFoundError: 
                print(f"{C.error} File not found (The path is correct?)")
                sys.exit(1)
    
        """ COLLECTING LINK """
        
        while True:
            try:
                self.link = input(f"{C.info} Link of the exercise: ").strip()  
                status_code = requests.get(self.link).status_code
                break
            except requests.exceptions.MissingSchema: 
                print(f"{C.error} Invalid Link. Did you forgot http(s)://?")
            

        if status_code not in [403, 200]:
            print(f"{C.error} Invalid Link. ")
        
        
        self.number = self.link[-4] + self.link[-3] + self.link[-2] + self.link[-1]
        
        with open("user-info/info.json") as file:
            content = file.read()
            content = json.loads(content)

        self.name = content["name"]
        self.contact = content["github"]

    def create_header(self):
        ext = open("functions/extensions.json", 'r')
        ext = ext.read()
        dictExt = json.loads(ext)

        for extension in dictExt:
            if self.path.endswith(extension):
                commentTag = dictExt[extension][0]
                openTag = dictExt[extension][1]
                closeTag = dictExt[extension][2]
                self.endfile = extension

        header  = f"{openTag} QUEENBEE: github.com/entr0pie/QUEENBEE {closeTag}\n"
        header += f"{commentTag} Date: {str(date.today())}\n"
        header += f"{commentTag} Source: {self.link}\n"
        header += f"{commentTag} Author: {self.name}\n"
        header += f"{commentTag} Contact: <{self.contact}>\n"
        header += f"{commentTag} Name: BEE {self.number}"

        line = ""
        for l in range(len(f"{commentTag} Source: {self.link}")):
            line += "="
        
        print('\n' + line)
        print(header)
        print(line + '\n')

        isOk = input(f"{C.warn} The information is correct? [Y/n] ").strip().upper()

        header += "\n\n"

        if isOk == "" or isOk == "Y":
            print(f"{C.win} Writing...")
            return header
        else:
            RegisterExercise(self.path)

