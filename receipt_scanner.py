from PIL import Image
from pytesseract import image_to_string
import pytesseract


def scan_receipt():
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    groceries = image_to_string(Image.open("bonnetje.jpg"))
    groceries=groceries.splitlines()
    groceries= ["jumbo " + item for item in groceries]
    return groceries