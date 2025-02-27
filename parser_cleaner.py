import os
import re
from tkinter import Tk, filedialog

def choose_file():
    root = Tk()
    root.withdraw()
    return filedialog.askopenfilename(title="Bir TXT dosyası seçin", filetypes=[("Text files", "*.txt")])

def clean_file():
    input_file = choose_file()
    if not input_file:
        print("Dosya seçilmedi, işlem iptal edildi.")
        return

    output_file = f"{os.path.splitext(input_file)[0]}_cleaned.txt"

    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    cleaned_lines = []
    for line in lines:
        cleaned_line = re.sub(r'https?://\S+|www\.\S+', '', line).strip()
        print(f"Orijinal: {line.strip()}\nTemizlenmiş: {cleaned_line.strip()}")

        if cleaned_line:
            cleaned_lines.append(cleaned_line + "\n")

    if cleaned_lines:
        with open(output_file, "w", encoding="utf-8") as file:
            file.writelines(cleaned_lines)
        print(f"URL'ler temizlendi. Yeni dosya: {output_file}")
    else:
        print("Dosyada geçerli veri bulunamadı.")

if __name__ == "__main__":
    clean_file()