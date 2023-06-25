import cv2

class EdgeDetector:
    def __init__(self):
        pass

    def detect_edges(self, image_path):
        """
        Detects edges in an image using a lightweight algorithm.
        """
        img = cv2.imread(image_path, 0)
        edges = cv2.Canny(img, 100, 200)
        cv2.imwrite("edges.jpg", edges)
