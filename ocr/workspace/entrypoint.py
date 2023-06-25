import os
from ocr import OCR
from file_manager import FileManager

def main():
    # Get folder location from user
    folder_location = input("Enter folder location: ")

    # Instantiate OCR and FileManager classes
    ocr = OCR()
    file_manager = FileManager()

    # Loop through all .jpg files in folder
    for filename in os.listdir(folder_location):
        if filename.endswith(".jpg"):
            # Load image file
            image = file_manager.load_image_file(os.path.join(folder_location, filename))

            # Process image and extract text
            ocr.load_image(image)
            ocr.process_image()
            text = ocr.extract_text()

            # Save text file
            file_manager.save_text_file(text, os.path.join(folder_location, filename.replace(".jpg", ".txt")))

if __name__ == "__main__":
    main()
