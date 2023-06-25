from image_converter import ImageConverter
from edge_detector import EdgeDetector
from color_subdivider import ColorSubdivider
from paint_by_number_generator import PaintByNumberGenerator
from database_manager import DatabaseManager
from frontend import Frontend

if __name__ == "__main__":
    # Initialize objects
    image_converter = ImageConverter()
    edge_detector = EdgeDetector()
    color_subdivider = ColorSubdivider()
    paint_by_number_generator = PaintByNumberGenerator()
    database_manager = DatabaseManager()
    frontend = Frontend()

    # Run application
    frontend.run()
