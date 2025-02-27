import os
import re
from tkinter import Tk, filedialog

def choose_directory():
    root = Tk()
    root.withdraw()
    return filedialog.askdirectory(title="Bir klasör seçin")

def search_in_files(directory):
    search_terms = input("Aramak istediğiniz kelimeleri virgülle ayırarak girin: ").strip().split(',')
    if not search_terms:
        return

    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.txt')]
    if not files:
        return

    for term in search_terms:
        term = term.strip()
        if not term:
            continue

        output_name = re.sub(r'[<>:"/\\|?*]', '_', f"{term}_results.txt")
        counter = 1
        while os.path.exists(output_name):
            output_name = f"{term}_results_{counter}.txt"
            counter += 1

        with open(output_name, "w", encoding="utf-8") as output:
            for file in files:
                try:
                    with open(file, "r", encoding="utf-8", errors="ignore") as f:
                        matches = [line for line in f if term in line]
                        if matches:
                            output.writelines(matches)
                except UnicodeDecodeError:
                    pass

def main():
    directory = choose_directory()
    if directory:
        search_in_files(directory)

main()