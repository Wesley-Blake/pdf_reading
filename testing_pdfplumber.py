from pathlib import Path
import pdfplumber

DIR = 'some place'

def invoice_number(file) -> int:
    invoice_number = 0
    with pdfplumber.open(file) as pdf:
        for line in pdf.pages[0].extract_text_lines():
            if 'invoice' in line['text'].lower() and 'date' not in line['text'].lower():
                first_space = line['text'].rfind(' ')+1
                invoice_number = line['text'][first_space:]
                break
    return invoice_number

def main():
    invoice_dir = Path(DIR)

    for file in invoice_dir.iterdir():
        if file.is_file() and file.name.lower().endswith('.pdf'):
            print(f"{file.name}: {invoice_number(file)}")


if __name__ == '__main__':
    main()
