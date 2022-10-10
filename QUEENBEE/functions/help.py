from colorama import Fore, Style

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
    text += "     -g | --get            Get any resolution from the oficial repository.\n"
    text += "                             (ex: python3 queenbee.py -g 1084.py)\n"
    text += "\n---------------------------------------------------------------------------------\n\n"
    text += "   OPTIONS:\n"
    text += "   [SEARCH SECTION]\n"
    text += "     --link your_link      Do the search (local) by a beecrowd link.\n\n"
    text += "   [GET SECTION]\n"
    text += "     -o | --out myFile.c   Output an Get-Request to a local file.\n"



    print(text)
