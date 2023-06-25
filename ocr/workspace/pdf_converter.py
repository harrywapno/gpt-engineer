import os
from PIL import Image
from pdfminer.high_level import extract_text


class PDFConverter:
    def __init__(self, image_path: str):
        self.image_path = image_path

    def convert_to_pdf(self):
        pdf_path = self._get_pdf_path()
        with Image.open(self.image_path) as image:
            image.save(pdf_path, 'PDF', resolution=100.0)

    def _get_pdf_path(self) -> str:
        pdf_path = os.path.splitext(self.image_path)[0] + '.pdf'
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
        return pdf_path
