import os
import pdfplumber

DIR = 'some place'


def pdf_search(dirpath, file, find_me):
    all_text = ""
    path = os.path.join(dirpath, file)
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            all_text += page.extract_text() + '\n'
    if find_me in all_text:
        print(path)


def main():
    path = input("Path of interest: ")
    if not os.path.isfile(path): SystemExit(1)
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            if file.endswith(".pdf"):
                pdf_search(dirpath, file, "P0520504")


if __name__ == '__main__':
    main()
