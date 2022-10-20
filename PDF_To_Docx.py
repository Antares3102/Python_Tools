from pdf2docx import Converter

file = str(input("Enter file name: ")) 

pdf_file = file + '.pdf'
docx_file = file + '.docx'

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()

print("\nSuccessfully!")