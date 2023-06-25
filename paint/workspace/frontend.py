from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from image_converter import ImageConverter
from edge_detector import EdgeDetector
from color_subdivider import ColorSubdivider
from paint_by_number_generator import PaintByNumberGenerator
from database_manager import DatabaseManager

class Frontend:
    def __init__(self):
        self.window = Tk()
        self.window.title("Paint By Number Generator")
        self.window.geometry("500x500")

        self.image_converter = ImageConverter()
        self.edge_detector = EdgeDetector()
        self.color_subdivider = ColorSubdivider()
        self.paint_by_number_generator = PaintByNumberGenerator()
        self.database_manager = DatabaseManager()

        self.image_path = None
        self.difficulty = None

        self.create_widgets()

    def create_widgets(self):
        """
        Creates the user interface widgets.
        """
        # Image selection button
        self.select_image_button = Button(self.window, text="Select Image", command=self.select_image)
        self.select_image_button.pack(pady=10)

        # Difficulty selection scale
        self.difficulty_label = Label(self.window, text="Select Difficulty")
        self.difficulty_label.pack()
        self.difficulty_scale = Scale(self.window, from_=2, to=10, orient=HORIZONTAL)
        self.difficulty_scale.pack()

        # Generate paint by number button
        self.generate_button = Button(self.window, text="Generate Paint By Number", command=self.generate_paint_by_number)
        self.generate_button.pack(pady=10)

        # Image listbox
        self.image_listbox = Listbox(self.window)
        self.image_listbox.pack(pady=10)
        self.populate_image_listbox()

    def select_image(self):
        """
        Opens a file dialog to select an image.
        """
        self.image_path = filedialog.askopenfilename(initialdir="/", title="Select Image", filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
        messagebox.showinfo("Image Selected", "Image selected successfully.")

    def generate_paint_by_number(self):
        """
        Generates a paint by number image based on the selected image and difficulty.
        """
        if self.image_path is None:
            messagebox.showerror("Error", "Please select an image.")
            return
        self.difficulty = self.difficulty_scale.get()
        self.image_converter.convert_to_jpeg(self.image_path)
        self.edge_detector.detect_edges("converted_image.jpeg")
        self.color_subdivider.subdivide_colors("edges.jpg", self.difficulty)
        self.paint_by_number_generator.generate_paint_by_number("color_subdivided_image.jpg", self.difficulty)
        self.database_manager.insert_image("Paint By Number Image", "paint_by_number_image.jpg", self.difficulty)
        messagebox.showinfo("Paint By Number Generated", "Paint by number image generated successfully.")
        self.populate_image_listbox()

    def populate_image_listbox(self):
        """
        Populates the image listbox with all images in the database.
        """
        self.image_listbox.delete(0, END)
        images = self.database_manager.get_images()
        for image in images:
            self.image_listbox.insert(END, f"{image[1]} - Difficulty: {image[3]}")

    def run(self):
        """
        Runs the frontend application.
        """
        self.window.mainloop()
