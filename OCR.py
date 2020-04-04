import cv2
import pytesseract
from PIL import Image

cap = cv2.VideoCapture(0)
while(True):
    ret,frame = cap.read()
    cv2.imshow('frame',frame)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(frame)
    print(text)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    