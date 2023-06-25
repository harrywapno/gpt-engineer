import os
import cv2
import numpy as np
import pytesseract


class ImageProcessor:
    def __init__(self, lang='eng'):
        self.lang = lang

    def process_image(self, image_path):
        # Load image
        image = cv2.imread(image_path)

        # Preprocess image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 3)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        # Perform OCR
        text = pytesseract.image_to_string(gray, lang=self.lang)

        # Save text to file
        text_path = os.path.splitext(image_path)[0] + '.txt'
        with open(text_path, 'w') as f:
            f.write(text)

    def process_images(self, folder_path):
        # Get list of image files in folder
        image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if
                       os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg'))]

        # Process each image
        for image_file in image_files:
            self.process_image(image_file)
