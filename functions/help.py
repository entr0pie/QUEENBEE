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
    text += f"USAGE: python3 {Fore.YELLOW}queenbee.py{Style.RESET_ALL} {Fore.MAGENTA}[MODE]{Style.RESET_ALL} {Fore.CYAN}[OPTIONS]{Style.RESET_ALL}\n\n"
    text += f"  {Fore.MAGENTA}MODE:{Style.RESET_ALL}\n"
    text += "     -r | --register path  Register a new solution.\n"
    text += "     -s | --search term    Search for an specific exercise\n"
    text += "                             (ex: python3 queenbee.py -s 1084)\n"
    text += "\n---------------------------------------------------------------------------------\n\n"
    text += f"  {Fore.CYAN}OPTIONS:{Style.RESET_ALL}\n"
    text += "   [SEARCH SECTION]         [DESCRIPTION]\n"
    text += "     --link your_link       Do the search by a beecrowd link.\n"
    text += "     -o  | --output file    Download the code to an file.\n"


    print(text)
