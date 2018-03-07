import pytesseract
from PIL import Image
import cv2
import os


image = cv2.imread("image.png") #place whatever image you want the text to be read from within the paranthesis.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
gray = cv2.medianBlur(gray,3)
filename = '{}.png'.format(os.getpid())
cv2.imwrite(filename,gray)
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)





