from os import system, listdir, path

from functions.beecolors import Colors

C = Colors()

class BeeSearch:
    def __init__(self, term):
        self.term = term

    def id_search(self):
        print(f"{C.info} SEARCHING FOR {self.term}...")

        folderExists = path.exists(f"ex/{self.term}")
        
        if folderExists == True:
            files = listdir(f"ex/{self.term}")
            
            if len(files) == 1:
                found_text = f"{C.win} FOUND {files[0]} (PATH: QUEENBEE/ex/{self.term}/{files[0]})\n"
                print(found_text)

                line = ""
                semiline = ""
                
                for l in range(len(found_text)):
                    line += "="
                    semiline += "-"

                print(line)
                script = open(f"ex/{self.term}/{files[0]}", 'r')
                lines = script.readlines()
                
                for h in range(6):
                    lines[h] = lines[h].replace("\n", "", 1)
                    print(lines[h])

                print(semiline + '\n')

                for l in range(7, len(lines)):
                    lines[l] = lines[l].replace("\n", "", 1)
                    print(lines[l])

                print('\n' + semiline)
                print(line)
        else:
            pass

    def link_search(self):
        print(f"{C.info} SEARCHING LINK: {self.term}")
        self.term = self.term[-4] + self.term[-3] + self.term[-2] + self.term[-1]
        self.id_search()

