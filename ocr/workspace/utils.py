import os
from typing import List

def get_image_files(folder_path: str) -> List[str]:
    # get list of files in folder
    files = os.listdir(folder_path)

    # filter for image files
    image_files = [os.path.join(folder_path, file) for file in files if file.endswith('.jpg')]

    return image_files

def create_output_file_path(input_file_path: str, output_folder_path: str) -> str:
    # get input file name without extension
    input_file_name = os.path.splitext(os.path.basename(input_file_path))[0]

    # create output file path
    output_file_path = os.path.join(output_folder_path, input_file_name + '.txt')

    return output_file_path

def write_text_to_file(text: str, output_file_path: str):
    # write text to output file
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(text)
