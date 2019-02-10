# use pdfminer.six for python 3.X, this requires to install "chardet-3.0.4"
# use pdfminer for python 2.7

from PyPDF2 import PdfFileReader
import os
import re

mypath = os.getcwd()  #set directory containing PDFs
print("PDF files in the directory -> ", mypath, "\n")

count = 0
fullText = "" #set as "empty" string
genes = ""

for pdfFile in os.listdir(mypath):
    if pdfFile.endswith(".pdf"):
        count+=1
        print("File ", pdfFile)
        textFileName = pdfFile.split(".")
        textFileName = textFileName[0]+".csv" #set txt/csv format
# Open PDF file
        openpdf = PdfFileReader(pdfFile, 'rb') # "rb" read binary
        nbPages = openpdf.numPages
# Convert PDF file into flat text
        for page in range(nbPages):
            print("Reading page",page+1," of ", nbPages)
            pageObj = openpdf.getPage(page)
            text= pageObj.extractText()
            fullText = fullText + text
        #print(fullText))
# Use REGEX to get genes with the format: SAUSA300_XXXX
# where XXXX means 4 digits
        match = re.findall('^SAUSA300_\d{4}', fullText, re.MULTILINE) #re.MULTILINE scans over the long string
        match = sorted(set(match)) #remove duplicates
        match = '\n'.join(map(str, match)) # convert list into string
        print("\n \n List of genes: \n \n",match)
# Export text as txt/csv files
        output= open(textFileName ,"w+")
        output.write(match)
        output.close()
