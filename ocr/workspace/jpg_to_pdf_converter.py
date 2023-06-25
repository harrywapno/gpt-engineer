import os
import glob
from PIL import Image
import pytesseract
from pdf2image import convert_from_path


class JpgToPdfConverter:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path

    def convert_to_pdf(self, file_path: str):
        """
        Converts a single .jpg file to .pdf format.
        """
        img = Image.open(file_path)
        pdf_path = os.path.splitext(file_path)[0] + ".pdf"
        img.save(pdf_path, "PDF", resolution=100.0)
        print(f"Converted {file_path} to {pdf_path}")

    def convert_to_text(self, file_path: str):
        """
        Converts a single .jpg file to .txt format.
        """
        img = Image.open(file_path)
        text_path = os.path.splitext(file_path)[0] + ".txt"
        text = pytesseract.image_to_string(img)
        with open(text_path, "w") as f:
            f.write(text)
        print(f"Converted {file_path} to {text_path}")

    def convert_all(self):
        """
        Converts all .jpg files in the specified folder to .pdf and .txt formats.
        """
        jpg_files = glob.glob(os.path.join(self.folder_path, "*.jpg"))
        if not jpg_files:
            print(f"No .jpg files found in {self.folder_path}")
            return
        for file_path in jpg_files:
            self.convert_to_pdf(file_path)
            self.convert_to_text(file_path)


def main():
    folder_path = "Users/Harry/Source/Repos/gpt-engineer/ocr/workspace"
    converter = JpgToPdfConverter(folder_path)
    converter.convert_all()


if __name__ == "__main__":
    main()
