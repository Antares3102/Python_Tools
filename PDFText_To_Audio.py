import PyPDF3
import pyttsx3

file = str(input("Enter file name: "))

file_path = file + '.pdf'

path = open(file_path, 'rb')

pdfReader = PyPDF3.PdfFileReader(path)

speak = pyttsx3.init()

for pages in range(pdfReader.numPages):
	if int(pages) > 0 and int(pages)%10 == 0:
		print("Processing... " + int(pages) + "/" + int(pdfReader.numPages))
	text = pdfReader.getPage(pages).extractText()
	speak.say(text)
	speak.runAndWait()
speak.stop()