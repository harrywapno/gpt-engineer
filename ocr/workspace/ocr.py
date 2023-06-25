import pytesseract
import cv2

class OCR:
    def __init__(self):
        """
        Initializes the OCR object
        """
        # Set up OCR engine
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        self.config = ("-l pol --oem 1 --psm 3")

    def extract_text(self, image_path: str) -> str:
        """
        Extracts text from the specified image file using OCR
        """
        # Load image
        image = cv2.imread(image_path)

        # Convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to remove noise
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        # Perform OCR
        text = pytesseract.image_to_string(thresh, config=self.config)

        return text
