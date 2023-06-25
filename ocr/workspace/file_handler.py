import os

def get_image_files(folder_path):
    """
    Returns a list of image files in the specified folder path
    """
    image_files = []
    for file in os.listdir(folder_path):
        if file.endswith(".jpg"):
            image_files.append(os.path.join(folder_path, file))
    return image_files

def create_output_file(file_path, text):
    """
    Creates a plain text file with the extracted text at the specified file path
    """
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
