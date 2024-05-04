import pytesseract
from PIL import Image

# Path to the Tesseract executable (change this according to your installation)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Path to the image file
image_path = r"C:\Users\crist\Desktop\Cristian mest bild\Skärmbild 2024-05-02 130859.png"


def ImgtoText():
    # Perform OCR on the image
    output = pytesseract.image_to_string(Image.open(image_path))
    return output
# Print the extracted text
print(ImgtoText())
