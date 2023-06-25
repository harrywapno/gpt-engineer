import cv2
import os
from movie import Movie
from gif import GIF

def generate_gifs(movie: Movie) -> None:
    # Load movie
    cap = cv2.VideoCapture(movie.file_path)

    # Get total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Generate GIFs in increments of 42 frames
    for i in range(0, total_frames, 42):
        # Set frame position
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)

        # Read frame
        ret, frame = cap.read()

        # Save frame as GIF
        # ...

    # Create folder for GIFs
    os.mkdir(movie.title)

    # Move GIFs to folder
    # ...

    # Create GIF objects
    gifs = []
    for gif_file in gif_files:
        gif = GIF(title=movie.title, file_path=gif_file)
        gifs.append(gif)
