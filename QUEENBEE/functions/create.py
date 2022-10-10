from datetime import date

import requests

from functions.beecolors import Colors

C = Colors()

class CreateExercise:
    def __init__(self, args=None):
        self.args = args

        self.collect_data()
        
        header = self.create_header()
        newFile = open(f"ex/{self.number}{self.endfile}", 'x')
        newFile.write(header)
        newFile.write(self.fileContent)
    
    def collect_data(self):
        
        # GET LINK
        while True:
            self.link = input(f"{C.info} Link of the exercise: ").strip()  
            
            status_code = requests.get(self.link).status_code
            if status_code in [403, 200]:
                break  
            else:
                print(f"{C.error} Invalid Link. ")
        
        self.number = self.link[-4] + self.link[-3] + self.link[-2] + self.link[-1]

        self.fileName = input(f"{C.info} File name: ").strip() 
        self.fileContent = open(self.fileName, 'r')
        self.fileContent = self.fileContent.read()
        
        self.name = input(f"{C.info} Your name: ").strip()
        self.contact = input(f"{C.info} Contact (Github link or Email): ").strip()


    def create_header(self):
        commentTag = "//"
        
        if self.fileName.endswith(".py"):
            self.endfile = ".py"
            commentTag = "#"
            openTag, closeTag = "\"\"\"", "\"\"\""

        if self.fileName.endswith(".c"):
            self.endfile = ".c"
            commentTag = "//"
            openTag, closeTag = "/*", "*/"

        header  = f"{openTag} BEECROWN: gitlink {closeTag}\n"
        header += f"{commentTag} Date: {str(date.today())}\n"
        header += f"{commentTag} Source: {self.link}\n"
        header += f"{commentTag} Author: {self.name}\n"
        header += f"{commentTag} Contact: <{self.contact}>\n"
        header += f"{commentTag} Name: BEE {self.number}"

        print("\n=============================")
        print(header)
        print("=============================\n")


        isOk = input(f"{C.warn} Ok? [Y/n] ").strip().upper()

        header += "\n\n"

        if isOk == "" or isOk == "Y":
            print(f"{C.win} Writing...")
            return header
        else:
            CreateExercise(self.args)

