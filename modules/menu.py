from .utils import Utils
from .ascii_art import AsciiArt

class Menu:
    def __init__(self):
        self.utils = Utils()
        self.ascii_art = AsciiArt()

    def display_prompt(self) -> str:
        header = "╔══════[OBLIVION ♡ antilag & goxdev]"
        footer = "╚════ ➤ "

        gradient_header = self.utils.gradient_text(
            header,
            (255, 0, 0),
            (255, 165, 0),
            direction="left"
        )
        
        gradient_footer = self.utils.gradient_text(
            footer,
            (255, 0, 0),
            (255, 165, 0),
            direction="left"
        )

        return input(f"\n{gradient_header}\n{gradient_footer}")

    def handle_commands(self):
        while True:
            try:
                self.utils.clear()
                self.ascii_art.display()
                choice = self.display_prompt()
                
                if choice == "1":
                    self.combo_optimizer()
                elif choice == "2":
                    self.combo_finder()
                elif choice.lower() in ['exit', 'quit', 'q', 'cikis']:
                    Utils.clear()
                    print("\nthanks for using Oblivion! <3")
                    break
                else:
                    print(f"command not found: {choice}")
                    
            except KeyboardInterrupt:
                Utils.clear()
                print("\nthanks for using Oblivion! <3")
                break

    def combo_optimizer(self):
        self.utils.clear()
        print("Combo Optimizer")
        input("press enter...")
        
        
    def combo_finder(self):
        self.utils.clear()
        print("Combo Finder") 
        input("press enter...") 