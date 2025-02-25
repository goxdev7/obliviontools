from os import system, name
from time import sleep
from typing import Tuple

class Utils:
    @staticmethod
    def clear() -> None:
        system('cls' if name == 'nt' else 'clear')

    @staticmethod
    def bomb() -> None:
        Utils.clear()
        frames = [
            """
            / **/|        
            | == /        
             |  |         
             |  |         
             |  /         
              |/  
            """,
            """
            / **/|        
            | == /        
             |  |         
             |  |         
             |  /         
              |/  
            """,
            """
            / **/|        
            | == /        
             |  |                  
            """,
            """
             _.-^^---....,,--       
         _--                  --_  
        <                        >)
        |                         | 
         \\._                   _./  
            ```--. . , ; .--'''       
                  | |   |             
               .-=||  | |=-.   
               `-=#$%&%$#=-'   
                  | ;  :|     
         _____.,-#%&$@%#&#~,._____
            """
        ]
        
        for frame in frames:
            Utils.clear()
            print(frame)
            sleep(0.6)
        
        Utils.clear()

    @staticmethod
    def gradient_text(
        text: str, 
        start_color: Tuple[int, int, int], 
        end_color: Tuple[int, int, int], 
        direction: str = "left"
    ) -> str:

        gradient_text = ""
        length = len(text)
        
        for i, char in enumerate(text):
            if direction == "left":
                r = start_color[0] + int((end_color[0] - start_color[0]) * (i / length))
                g = start_color[1] + int((end_color[1] - start_color[1]) * (i / length))
                b = start_color[2] + int((end_color[2] - start_color[2]) * (i / length))
            elif direction == "right":
                r = end_color[0] + int((start_color[0] - end_color[0]) * (i / length))
                g = end_color[1] + int((start_color[1] - end_color[1]) * (i / length))
                b = end_color[2] + int((start_color[2] - end_color[2]) * (i / length))
            
            gradient_text += f"\x1b[38;2;{r};{g};{b}m{char}"
            
        return gradient_text + "\x1b[0m"