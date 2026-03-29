import os
import sys
from colorama import Fore, Style

def visualize_directory(path):
    for root, dirs, files in os.walk(path):
        level = root.replace(path, "").count(os.sep)
        indent = " " * 4 * level
        print(f"{indent}{Fore.BLUE}{os.path.basename(root)}{Style.RESET_ALL}/")
        subindent = " " * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{Fore.GREEN}{f}{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Вкажіть шлях до директорії як аргумент.")
    else:
        directory_path = sys.argv[1]
        visualize_directory(directory_path)