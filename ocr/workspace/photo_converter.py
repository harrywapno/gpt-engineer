import os
from typing import List
from PIL import Image
from reportlab.lib.pagesizes import portrait
from reportlab.pdfgen import canvas
from ocr_engines import OCR

class PhotoConverter:
    def __init__(self, ocr_engine: OCR):
        self.ocr_engine = ocr_engine

    def convert_to_text(self, file_path: str) -> str:
        """
        Converts the photo at the specified path to plain text using the OCR engine.

        Args:
            file_path (str): The path to the photo.

        Returns:
            str: The plain text extracted from the photo.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found at {file_path}")

        text = self.ocr_engine.recognize(file_path)
        return text

    def convert_to_pdf(self, file_path: str, pdf_path: str) -> None:
        """
        Converts the photo at the specified path to a PDF file at the specified path.

        Args:
            file_path (str): The path to the photo.
            pdf_path (str): The path to save the PDF file.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found at {file_path}")

        # Open the image and get its dimensions
        with Image.open(file_path) as img:
            width, height = img.size

        # Create a new PDF file
        with open(pdf_path, "wb") as pdf_file:
            # Create a new PDF canvas with the same dimensions as the image
            c = canvas.Canvas(pdf_file, pagesize=portrait((width, height)))

            # Draw the image on the PDF canvas
            c.drawImage(file_path, 0, 0, width, height)

            # Save the PDF file
            c.save()
