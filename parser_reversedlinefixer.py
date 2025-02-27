import os
import re
from tkinter import Tk, filedialog

def choose_file():
    root = Tk()
    root.withdraw()
    return filedialog.askopenfilename(title="Bir TXT dosyası seçin", filetypes=[("Text files", "*.txt")])

def reverse_password_login_url():
    input_file = choose_file()
    if not input_file:
        print("Dosya seçilmedi, işlem iptal edildi.")
        return

    output_file = f"{os.path.splitext(input_file)[0]}_reversed.txt"

    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    reversed_lines = []
    for line in lines:
        reversed_line = re.sub(r'([^:]+):([^:]+):(https?://\S+)', r'\3:\2:\1', line).strip()
        print(f"Orijinal: {line.strip()} -> Ters: {reversed_line.strip()}")

        if reversed_line:
            reversed_lines.append(reversed_line + "\n")

    if reversed_lines:
        with open(output_file, "w", encoding="utf-8") as file:
            file.writelines(reversed_lines)
        print(f"Ters çevrildi: {output_file}")
    else:
        print("Dosyada geçerli veri bulunamadı.")

if __name__ == "__main__":
    reverse_password_login_url()