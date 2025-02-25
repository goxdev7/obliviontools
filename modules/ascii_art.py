from pystyle import Colors, Colorate
from .utils import Utils

class AsciiArt:
    def __init__(self):
        self.start_color_left = (255, 0, 0)
        self.end_color_left = (255, 165, 0)
        self.start_color_right = (230, 0, 0)
        self.end_color_right = (230, 165, 0)

    def create_info_gradient(self, text: str) -> str:
        mid_point = len(text) // 2
        left_half = text[:mid_point]
        right_half = text[mid_point:]

        gradient_left = Utils.gradient_text(left_half, self.start_color_left, self.end_color_left, "left")
        gradient_right = Utils.gradient_text(right_half, self.start_color_right, self.end_color_right, "right")

        return gradient_left + gradient_right

    @staticmethod
    def get_main_ascii(gradient_line: str) -> str:
        part1 = f'''
   ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════╦═╗
   ║ ╔══════════════════════════════════════════════════════════════════╗    ╔═════════════════════════════════╝ ║
   ║ ║ ../$$$$$$../$$......./$$./$$............/$$....................  ║    ║                                   ║
   ║ ║ ./$$__..$$|.$$......|.$$|__/...........|__/....................  ║    ║        \x1b[38;2;145;53;54m「   OPTIONS    」\x1b[38;2;255;100;100m         ║
   ║ ║ |.$$..\.$$|.$$$$$$$.|.$$./$$./$$..../$$./$$../$$$$$$../$$$$$$$.  ║    ║                                   ║
   ║ ║ |.$$..|.$$|.$$__..$$|.$$|.$$|..$$../$$/|.$$./$$__..$$|.$$__..$$  ║    ║                                   ║
   ║ ║ |.$$..|.$$|.$$..\.$$|.$$|.$$.\..$$/$$/.|.$$|.$$..\.$$|.$$..\.$$. ║    ║      ↠ 1. Combo Optimizer         ║
   ║ ║ |.$$..|.$$|.$$..|.$$|.$$|.$$..\..$$$/..|.$$|.$$..|.$$|.$$..|.$$. ║    ║      ↠ 2. Combo Finder            ║
   ║ ║ |..$$$$$$/|.$$$$$$$/|.$$|.$$...\..$/...|.$$|..$$$$$$/|.$$..|.$$. ║    ║                                   ║
   ║ ║ .\______/.|_______/.|__/|__/....\_/....|__/.\______/.|__/..|__/. ║    ║                                   ║
   ║ ║ ...............................................................  ║    ║                                   ║
   ║ ╚╦════════════════════════════════════════════════════════════════╦╝    ║                                   ║
   ║ ╔╩════════════════════════════════════════════════════════════════╩╗    ║                                   ║'''

        part2 = f'''
   ║ ║ {gradient_line} ║    ║                                   ║'''

        part3 = '''
   ║ ╚══════════════════════════════════════════════════════════════════╝    ║                                   ║
   ║                                                                         ║                                   ║
   ║                                                                         ║                                   ║
   ║                                                                         ║                                   ║
   ║                                                                         ║                                   ║
   ║                                                                         ║                                   ║  
   ║                                                                         ╚═════════════════════════════════╗ ║
   ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════╩═╝'''

        return part1 + part2 + part3

    def display(self) -> None:
        text_to_gradient = "██████████████████████████i̶ n̶ f̶ o̶███████████████████████████"
        gradient_line = self.create_info_gradient(text_to_gradient)
        ascii_art = self.get_main_ascii(gradient_line)
        print(Colorate.Vertical(Colors.red_to_white, ascii_art, cut=1))