import numpy as np
from sklearn.cluster import KMeans
from PIL import Image

class ColorSubdivider:
    def __init__(self):
        pass

    def subdivide_colors(self, image_path, num_colors):
        """
        Subdivides an image into a specified number of colors.
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
