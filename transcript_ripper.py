import pytesseract as tess
from PIL import Image
from pdf2image import convert_from_path
import os



CCL = 4 #class code length

def isID(num):
  global CCL
  if not len(num) == CCL:
    return False
  for x in range(CCL):
    digit = num[x]
    if digit == "1" or digit == "2" or digit == "3" or digit == "4" or digit == "5" or digit == "6" or digit == "7" or digit == "8" or digit == "9" or digit == "0":
      pass #we good
    else:
      return False
  return True

if os.path.exists("Page_1.jpg"):
  os.remove("Page_1.jpg")

pdfs = 'Sample Transcript 2.pdf'
pages = convert_from_path(pdfs, 350)

i = 1
for page in pages:
    image_name = "Page_" + str(i) + ".jpg"  
    page.save(image_name, "JPEG")
    i = i+1 

text = tess.image_to_string("Page_1.jpg", config = "-l ENG --psm 6")

classes = []
text = text.split()
output = ""
for index in range(len(text)):
  word = text[index]
  if isID(word):
    further = 1
    while not ".0000" in text[index + further] and not "5.000" in text[index + further] and not ".000" in text[index + further]:
      further += 1
    #class_name = " ".join(text[index:index+further-1])
    class_name = text[index + 1:index+further-1]
    grade = text[index+further-1]

    output += word + " "
    for hi in class_name:
      output += hi + " "
    output += grade + " "
    output += "\n"

f = open("output.txt", "w+")
f.write(output)
f.close()
  

