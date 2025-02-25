from colorama import Fore
from threading import Lock
from datetime import datetime

class Logger(object):
    def __init__(self):
        self.color_table = {
            "info": Fore.BLUE,
            "warning": Fore.YELLOW,
            "error": Fore.RED,
            "debug": Fore.MAGENTA
        }
        self.lock = Lock()

    def get_time(self):
        return f"{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET}"

    def lprint(self, message):
        with self.lock:
            print(message)

    def info(self, message):
        message = f"{self.get_time()} {self.color_table['info']}INF{Fore.RESET} {message}"
        self.lprint(message)

    def error(self, message):
        message = f"{self.get_time()} {self.color_table['error']}ERR{Fore.RESET} {message}"
        self.lprint(message)

    def warn(self, message):
        message = f"{self.get_time()} {self.color_table['warning']}WRN{Fore.RESET} {message}"
        self.lprint(message)

    def debug(self, message):
        message = f"{self.get_time()} {self.color_table['debug']}DBG{Fore.RESET} {message}"
        self.lprint(message)