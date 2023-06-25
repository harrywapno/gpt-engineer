import os
import pytesseract
from PIL import Image


class TextConverter:
    def __init__(self, image_path: str):
        self.image_path = image_path

    def convert_to_text(self):
        text_path = self._get_text_path()
        with Image.open(self.image_path) as image:
            text = pytesseract.image_to_string(image)
            with open(text_path, 'w') as f:
                f.write(text)

    def _get_text_path(self) -> str:
        text_path = os.path.splitext(self.image_path)[0] + '.txt'
        if os.path.exists(text_path):
            os.remove(text_path)
        return text_path
