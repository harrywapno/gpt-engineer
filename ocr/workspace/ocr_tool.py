import os
from typing import List
from PIL import Image
from pdf2image import convert_from_path
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from io import StringIO
import argparse


class ImageConverter:
    def __init__(self, image_path: str):
        self.image_path = image_path

    def convert_to_pdf(self) -> str:
        pdf_path = os.path.splitext(self.image_path)[0] + ".pdf"
        with Image.open(self.image_path) as img:
            img.save(pdf_path, "PDF", resolution=100.0)
        return pdf_path

    def convert_to_text(self, pdf_path: str) -> str:
        output_string = StringIO()
        with open(pdf_path, 'rb') as in_file:
            resource_manager = PDFResourceManager()
            laparams = LAParams()
            device = TextConverter(resource_manager, output_string, laparams=laparams)
            interpreter = PDFPageInterpreter(resource_manager, device)
            for page in PDFPage.get_pages(in_file, check_extractable=True):
                interpreter.process_page(page)
        text = output_string.getvalue()
        output_string.close()
        return text


def convert_images_to_pdf_and_text(image_folder: str) -> None:
    for file_name in os.listdir(image_folder):
        if file_name.endswith(".jpg"):
            image_path = os.path.join(image_folder, file_name)
            image_converter = ImageConverter(image_path)
            pdf_path = image_converter.convert_to_pdf()
            text = convert_pdf_to_text(pdf_path)
            text_path = os.path.splitext(pdf_path)[0] + ".txt"
            with open(text_path, "w") as text_file:
                text_file.write(text)


def convert_pdf_to_text(pdf_path: str) -> str:
    text = extract_text(pdf_path)
    return text


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JPG images to PDF and plain text")
    parser.add_argument("image_folder", type=str, help="Path to the folder containing JPG images")
    args = parser.parse_args()
    convert_images_to_pdf_and_text(args.image_folder)
