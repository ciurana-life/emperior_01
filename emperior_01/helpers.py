from datetime import datetime

from colorama import Fore, Style
from colorama import init as colorama_init

colorama_init()


def cprint(text: str, color: str) -> None:
    if color == "G":
        print(f"{Fore.GREEN}[#] {text}{Style.RESET_ALL}")
    if color == "R":
        print(f"{Fore.RED}[Error] {text}{Style.RESET_ALL}")


def validate_date_format(date_str: str) -> bool:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
