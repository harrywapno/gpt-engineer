import os
from pdf2image import convert_from_path
from ocr_model import OCRModel

class ImageConverter:
    def __init__(self, language='pol'):
        self.language = language
        self.ocr_model = OCRModel(language)

    def convert_image_to_pdf(self, image_path, pdf_path):
        pages = convert_from_path(image_path, 300)
        for i, page in enumerate(pages):
            page.save(f"{pdf_path}_{i}.pdf", 'PDF')

    def convert_pdf_to_text(self, pdf_path, text_path):
        with open(text_path, 'w', encoding='utf-8') as f:
            for i, page in enumerate(convert_from_path(pdf_path)):
                text = self.ocr_model.perform_ocr(page)
                f.write(f"Page {i+1}:\n{text}\n\n")

    def convert_images_to_text(self, folder_path):
        for file in os.listdir(folder_path):
            if file.endswith('.jpg'):
                image_path = os.path.join(folder_path, file)
                pdf_path = os.path.splitext(image_path)[0]
                text_path = f"{pdf_path}.txt"
                self.convert_image_to_pdf(image_path, pdf_path)
                self.convert_pdf_to_text(f"{pdf_path}_0.pdf", text_path)
                os.remove(f"{pdf_path}_0.pdf")
