import os
from tkinter import Tk, filedialog

def choose_file():
    root = Tk()
    root.withdraw()
    return filedialog.askopenfilename(title="Bir TXT dosyası seçin", filetypes=[("Text files", "*.txt")])

def remove_duplicate_lines():
    file_path = choose_file()
    if not file_path:
        print("Dosya seçilmedi, işlem iptal edildi.")
        return

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    seen = set()
    unique_lines = [line for line in lines if not (line in seen or seen.add(line))]

    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(unique_lines)

    print(f"{file_path} dosyasındaki tekrar eden satırlar kaldırıldı.")

if __name__ == "__main__":
    remove_duplicate_lines()