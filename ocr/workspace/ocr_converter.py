import io
import os
import subprocess
import tempfile

class OCRConverter:
    def __init__(self):
        self.language = 'pol'

    def convert_to_pdf(self, image_file):
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as f:
            pdf_file = f.name
        subprocess.run(['convert', '-density', '300', image_file, pdf_file])
        return pdf_file

    def convert_to_text(self, pdf_file):
        with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as f:
            text_file = f.name
        subprocess.run(['tesseract', pdf_file, text_file, '-l', self.language, '--oem', '1', '--psm', '3'])
        with io.open(text_file, 'r', encoding='utf-8') as f:
            text = f.read()
        os.remove(text_file)
        return text
