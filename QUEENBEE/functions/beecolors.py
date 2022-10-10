from colorama import Fore, Style

class Colors:
    def __init__(self):
        self.info = f"{Fore.BLUE}[**]{Fore.WHITE}{Style.RESET_ALL}" 
        self.warn = f"{Fore.YELLOW}[??]{Fore.WHITE}{Style.RESET_ALL}" 
        self.error = f"{Fore.RED}[!!]{Fore.WHITE}{Style.RESET_ALL}"
        self.win = f"{Fore.GREEN}[OK]{Fore.WHITE}{Style.RESET_ALL}" 
        self.option = f"{Fore.MAGENTA}[OP]{Style.RESET_ALL}" 
