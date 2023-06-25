import cv2
import pytesseract

class OCRModel:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.model = None

    def load_model(self):
        self.model = cv2.dnn.readNet(self.config_file)

    def run_ocr(self, image):
        self.model.setInput(cv2.dnn.blobFromImage(image, scalefactor=1.0, size=(3000, 3000), swapRB=True, crop=False))
        output = self.model.forward()
        text = pytesseract.image_to_string(output, lang='pol')
        return text
