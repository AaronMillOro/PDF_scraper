# use pdfminer.six for python 3.X, this requires to install "chardet-3.0.4"
# use pdfminer for python 2.7

from PyPDF2 import PdfFileReader
import os
#from os import listdir
#from os.path import isfile, join

mypath = os.getcwd()  #set directory containing PDFs
print("PDF files in the directory -> ", mypath, "\n")

count=0
fullText="" #set as "empty" string

for pdfFile in os.listdir(mypath):
    if pdfFile.endswith(".pdf"):
        count+=1
        print("File ", pdfFile)
        textFileName = pdfFile.split(".")
        textFileName = textFileName[0]+".csv" #set txt format
# Open PDF files
        openpdf = PdfFileReader(pdfFile, 'rb') # "rb" read binary
        nbPages = openpdf.numPages
# Convert PDFs files into flat text
        for page in range(nbPages):
            print("Page",page+1,"/", nbPages)
            pageObj = openpdf.getPage(page)
            text= pageObj.extractText()
            fullText = fullText + text
        # print(fullText)

# Export text as txt files
        output= open(textFileName ,"w+")
        output.write(fullText)
        output.close()



#cmd /k for %%i in (*) do "c:\pdftotext\pdf2txt.py" -o c:\pdftotext\txt\%%~ni.txt %%i

# convert PDF text into flat txt file
#pdf2txt.py -o testout.txt ArgRregulon.pdf

# REGEX for genes ^SAUSA300_[0-9][0-9][0-9][0-9]$
