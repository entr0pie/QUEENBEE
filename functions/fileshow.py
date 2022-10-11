class FileManipulation: 
    def showFile(self, file_content) -> None:
        lines = file_content.splitlines()
    
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


    def saveFile(self, file_content, path, ext="") -> None:
        print(path + ext)
        file = open(path + ext, 'x')
        file.write(file_content)

