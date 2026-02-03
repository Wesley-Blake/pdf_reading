import os
from pathlib import Path
import pdfplumber
import pandas as pd

def get_path():
    directory = Path().cwd() / "pdf_reading"
    path = Path()
    for i in directory.iterdir():
        if i.name.endswith(".txt"):
            path = i
    with open(path) as f:
        return f.readline()

def pdf_search(dirpath, file, find_me):
    all_text = ""
    path = os.path.join(dirpath, file)
    if not os.path.isfile(path):
        print(f"Failed to find file (check path): {path}")
        SystemExit(1)
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            all_text += page.extract_text() + '\n'
    if find_me in all_text:
        print(path)


def main():
    # get path from temp tracker.
    path = get_path()
    pd.read_excel(path)
    print(pd)
    #dataframe = pd.read_excel(path)
    #if not os.path.isfile(path): SystemExit(1)
    #for dirpath, dirnames, filenames in os.walk(path):
    #    pass


if __name__ == '__main__':
    main()
