from os import listdir, path
import json
import sys

from functions.beecolors import Colors
from functions.fileshow import FileManipulation

import requests

C = Colors()
F = FileManipulation()

class BeeSearch:
    def __init__(self, fileName, output):
        self.fileName = fileName
        self.output = output

    def search(self):
        
        if "http" in self.fileName:
            self.searchRepo(link=True)
        
        else:
            if self.searchLocal():
                sys.exit(0)

            self.searchRepo()

    def searchLocal(self):
        """ BUSCA NOS ARQUIVOS LOCAIS """
        print(f"{C.info} SEARCHING FOR {self.fileName}...")

        folderExists = path.exists(f"repo/{self.fileName}")
        
        if folderExists:
            files = listdir(f"repo/{self.fileName}")
            
            if len(files) >= 1:
                # TODO: Make select for more than one option;
                found_text = f"{C.win} FOUND {files[0]} (PATH: QUEENBEE/repo/{self.fileName}/{files[0]})\n"
                print(found_text)

                script = open(f"repo/{self.fileName}/{files[0]}", 'r')
                content = script.read()
                
                F.showFile(content)

                # SAVES AFTER
                if self.output:
                    F.saveFile(content, self.output)
                
                return True
                
        else:
            print(f"{C.warn} Could not find {self.fileName} in the local machine.")
            return False

        

    def __verifylink__(self, link):
        response = requests.get(link)
                
        if response.status_code == 404:
            return False

        return True

    def searchRepo(self, link=False):
        """ BUSCA NO REPOSITÓRIO GIT """
        if not link:
            
            print(f"{C.info} SEARCHING FOR {self.fileName}...")
            
            namefile = self.fileName
            self.extension = ""

            for char in range(len(self.fileName)):
                if self.fileName[char] == ".":
                    for c in range(char, len(self.fileName)):
                        self.extension += self.fileName[c]
            
            noExtension = False
            if self.extension == "":
                noExtension = True

            link = ""
            
            if noExtension: 
                extDict = open("functions/extensions.json")
                extDict = extDict.read()
                ext = json.loads(extDict)

                for key in ext:
                    link = f"https://raw.githubusercontent.com/entr0pie/QUEENBEE/main/QUEENBEE/repo/{namefile}/{namefile}{key}"
                    isValid = self.__verifylink__(link)
                    if isValid:
                        self.extension = key
                        break
                    
                if not isValid: 
                    print(f"{C.error} ERROR: COULD NOT FIND {self.fileName} IN THE OFICIAL REPOSITORY")
                    sys.exit(1)
                        
            else:
                link = f"https://raw.githubusercontent.com/entr0pie/QUEENBEE/main/QUEENBEE/ex/{namefile}/{namefile}{self.extension}"
                isValid = self.__verifylink__(link)
                if not isValid: 
                    print(f"{C.error} ERROR: COULD NOT FIND {self.fileName} IN THE OFICIAL REPOSITORY")
                    sys.exit(1)
                
            response = requests.get(link)
                
            print(f"{C.win} FOUND {self.fileName} > {link}\n")
            F.showFile(response.text)
        
        elif link:
            isInRepo = self.__verifylink__(self.fileName)
            
            if not isInRepo:
                print(f"{C.error} ERROR: COULD NOT FIND {self.fileName} IN THE OFICIAL REPOSITORY")
                sys.exit(1)
            
            response = requests.get(self.fileName)
            F.showFile(response.text)


        if self.output:
            F.saveFile(response.text, path=self.output, ext=self.extension)

