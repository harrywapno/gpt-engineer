from PIL import Image

class ImageConverter:
    def __init__(self):
        pass

    def convert_to_jpeg(self, image_path):
        """
        Converts any image to .jpeg format.
        """
        with Image.open(image_path) as im:
            im = im.convert("RGB")
            im.save("converted_image.jpeg", "JPEG")
