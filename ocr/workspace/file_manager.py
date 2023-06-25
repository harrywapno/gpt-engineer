import os

class FileManager:
    def load_image_file(self, filepath):
        # Load image file using OpenCV
        image = cv2.imread(filepath)

        return image

    def save_text_file(self, text, filepath):
        # Save extracted text to plain text file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
