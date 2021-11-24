from PIL import ImageGrab
import pytesseract
import winsound


pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Prajna Moorthy\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

while True:
    #Grabbing the Image of Caption
    im = ImageGrab.grab(bbox=(370,712,1564,901))
    
    #Keywords to keep a track of
    keyword = ['attendance','roll','number','42','prajna']
    
    #Converts image to text
    text = pytesseract.image_to_string(im, lang='eng')
    print(text.split())
    
    #Checks if the keyword is present in text
    if ((keyword[0] in text) or (keyword[1] and keyword[2] in text)):
        winsound.Beep(frequency=2500, duration=1000)
        print('Attendance has started')
    else:
        continue