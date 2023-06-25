from image_processor import ImageProcessor


if __name__ == '__main__':
    # Initialize image processor
    image_processor = ImageProcessor()

    # Process images in folder
    folder_path = '/path/to/folder'
    image_processor.process_images(folder_path)
