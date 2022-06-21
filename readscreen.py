import time
from PIL import ImageGrab, Image, ImageFilter  # screenshot
import pyautogui as pg
import pytesseract
from pytesseract import Output
import random
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# p1 = (700, 500)
# p2 = (900, 600)

pos1 = (770, 520)
pos2 = (850, 570)

def readPrompt(p1=(770, 520), p2=(850, 570)):
    cap =  ImageGrab.grab(bbox=(p1[0], p1[1], p2[0], p2[1]))  # screenshot
    cap = cap.convert('L')   # make grayscale
    # cap.show()
    # cap.save("C:\\Users\\Faisal\\Desktop\\bombparty\\" + str(random.randint(1,100000000)) + pytesseract.image_to_string(cap).strip() + '.png')
    cap = cap.filter(ImageFilter.MinFilter)
    prompt = pytesseract.image_to_string(cap).strip()
    # cap.save("C:\\Users\\Faisal\\Desktop\\bombparty\\" + str(random.randint(1,100000000)) + '.png')
    return prompt

# print(readPrompt())

img = Image.open(r'C:\Users\Faisal\Desktop\bombparty\IA.png').convert('L')
img = img.filter(ImageFilter.MinFilter(3))
img = img.filter(ImageFilter.SHARPEN)
img.show()
print(pytesseract.image_to_string(img))
