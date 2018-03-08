import pytesseract
from PIL import Image
import cv2
import os


image = cv2.imread("image.png") #place whatever image you want the text to be read from within the paranthesis.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # converts image to grey scale whi
gray = cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] #establish the threshold
gray = cv2.medianBlur(gray,3) #this is optional and can be deleted or commented out. play around with it to get the desired ouput
filename = '{}.png'.format(os.getpid()) 
cv2.imwrite(filename,gray) #create a temp file
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract' #add the tesseract OCR engine to the mix
text = pytesseract.image_to_string(Image.open(filename)) #apply the temp file to to the tesseract engine to convert text within image 
os.remove(filename) #delete the temp file
print(text) #display output





