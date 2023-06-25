import numpy as np
from PIL import Image

class PaintByNumberGenerator:
    def __init__(self):
        pass

    def generate_paint_by_number(self, image_path, num_colors):
        """
        Generates a paint by number image based on the color-subdivided image.
        """
        with Image.open(image_path) as im:
            im = im.convert("RGB")
            im_array = np.array(im)
            im_array = im_array.reshape((im_array.shape[0] * im_array.shape[1], 3))
            kmeans = KMeans(n_clusters=num_colors, random_state=0).fit(im_array)
            new_im_array = kmeans.cluster_centers_[kmeans.labels_]
            new_im_array = new_im_array.reshape((im.size[1], im.size[0], 3))
            new_im = Image.fromarray(np.uint8(new_im_array))
            new_im.save("color_subdivided_image.jpg")

            # Generate paint by number image
            pb_image = Image.new("RGB", im.size)
            pb_pixels = pb_image.load()
            for i in range(im.size[0]):
                for j in range(im.size[1]):
                    color = tuple(new_im_array[j][i])
                    pb_pixels[i, j] = color
            pb_image.save("paint_by_number_image.jpg")
