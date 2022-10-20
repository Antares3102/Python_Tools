from PIL import Image

# file = str(input("Enter file name: "))
# file = file + 
Image.open("1.png")

import pywhatkit
pywhatkit.image_to_ascii_art('1.png', 'MyArt')
read_file = open("MyArt.txt", "r")
print(read_file.read())