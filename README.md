# PDF scraper
This PDF scraper was developed to select gene names in PDF files generated from "RegPrecise", a collection of manually curated inferences of Regulons in prokaryotic Genomes (http://regprecise.lbl.gov/RegPrecise/).

This script is adapted to select "SAUSA300_XXXX" genes. But it can be modified to select specific text patterns.

## Scraper functionalities 
* The script is capable to read all the PDF files in the working directory
* The text present on each PDF will be read and converted into flat text with the help of **PyPDF2** library (https://pypi.org/project/PyPDF2/)
* The script will search text with the Gene Identifier pattern “SAUSA300_XXXX”, where XXXX is a chain of 4 numbers
* Duplicated genes will be removed in order to generate a list of unique genes
* The list will be exported as CSV file for each PDF file
