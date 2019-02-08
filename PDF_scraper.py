# use pdfminer.six for python 3.X, this requies to install "chardet-3.0.4"
# use pdfminer for python 2.7

import PyPDF2
import os
from os import listdir
from os.path import isfile, join

mypath = os.getcwd()  #set directory containing PDFs
print("PDF files in the directory -> ", mypath, "\n")

# Convert PDF into text
count=0
for file in os.listdir(mypath):
    if file.endswith(".pdf"):
        count+=1
        print(count, file)
    #    pdf2txt.py -o count.txt file

# convert PDF text into flat txt file
# pdf2txt.py -o testout.txt ArgRregulon.pdf

# REGEX for genes ^SAUSA300_[0-9][0-9][0-9][0-9]$
