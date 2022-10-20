# importing library

from langdetect import detect 

# taking input from user 
text = input("Enter any text in any language: ")

# printing output
print(detect(text))