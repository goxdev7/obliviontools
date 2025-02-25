from modules.logger import Logger
from modules.menu import Menu
from modules.utils import Utils

def main():
    logger = Logger()
    menu = Menu()
    
    Utils.clear()
    
    menu.handle_commands()

if __name__ == "__main__":
    main()