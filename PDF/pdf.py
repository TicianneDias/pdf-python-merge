import os
from glob import glob
from PyPDF2 import PdfFileMerger


def pdf_merge():
    merger = PdfFileMerger()
    arquivos = [a for a in glob('*.pdf')]
    [merger.append(pdf, pages=(1, 2)) for pdf in arquivos]
    with open('nomepdf.pdf', 'wb') as new_file:
        merger.write(new_file)


if __name__ == '__main__':
    pdf_merge()
