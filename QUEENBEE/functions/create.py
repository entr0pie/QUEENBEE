from datetime import date
from os import system
import json

import requests

from functions.beecolors import Colors

C = Colors()

class CreateExercise:
    def __init__(self, args=None):
        self.args = args

        self.collect_data()
        
        header = self.create_header()

        system(f"mkdir ex/{self.number}")
        newFile = open(f"ex/{self.number}/{self.number}{self.endfile}", 'x')
        newFile.write(header)
        newFile.write(self.fileContent)
    
    def collect_data(self):
        while True:
            try:
                self.link = input(f"{C.info} Link of the exercise: ").strip()  
                status_code = requests.get(self.link).status_code
                break
            except requests.exceptions.MissingSchema: 
                print(f"{C.error} Invalid Link. Did you forgot http(s)://?")
            

        if status_code in [403, 200]:
            pass
        
        else:
            print(f"{C.error} Invalid Link. ")
        
        self.number = self.link[-4] + self.link[-3] + self.link[-2] + self.link[-1]

        while True:
            try:
                self.fileName = input(f"{C.info} File name: ").strip() 
                self.fileContent = open(self.fileName, 'r')
                self.fileContent = self.fileContent.read()
                break;
            
            except FileNotFoundError: 
                print(f"{C.error} File not found (The path is correct?)")
        
        self.name = input(f"{C.info} Your name: ").strip()
        self.contact = input(f"{C.info} Contact (Github link or Email): ").strip()

    def create_header(self):
        ext = open("functions/extensions.json", 'r')
        ext = ext.read()
        dictExt = json.loads(ext)

        for extension in dictExt:
            if self.fileName.endswith(extension):
                commentTag = dictExt[extension][0]
                openTag = dictExt[extension][1]
                closeTag = dictExt[extension][2]
                self.endfile = extension

        header  = f"{openTag} BEECROWN: https://github.com/entr0pie/QUEENBEE {closeTag}\n"
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
            CreateExercise(self.args)

