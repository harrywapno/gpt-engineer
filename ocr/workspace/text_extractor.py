import os
import pytesseract
from ocr_engines import OCR

class TesseractOCR(OCR):
    def recognize(self, file_path: str) -> str:
        """
        Recognizes text from the specified file using Tesseract OCR.

        Args:
            file_path (str): The path to the file.

        Returns:
            str: The recognized text.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found at {file_path}")

        text = pytesseract.image_to_string(file_path, lang='pol')
        return text

class TextExtractor:
    def __init__(self, ocr_engine: OCR):
        self.ocr_engine = ocr_engine

    def extract_text(self, file_path: str) -> str:
        """
        Extracts text from the specified file using the OCR engine.

        Args:
            file_path (str): The path to the file.

        Returns:
            str: The extracted text.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found at {file_path}")

        text = self.ocr_engine.recognize(file_path)
        return text
