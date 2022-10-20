import PyPDF3
import pyttsx3

file = str(input("Enter file name: "))

pdfReader = PyPDF.PdfFileReader(open(file + '.pdf', 'rb'))

speaker = pyttsx3.init()

for page_num in range(pdfReader.numPages):
	text = pdfReader.getPage(page_num).extractText()
	speaker.say(text)
	speaker.runAndWait()

speaker.stop()

engine.save_to_file(text, 'C:\Users\overl\Downloads\audio.mp3')
engine.runAndWait()