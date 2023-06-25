Core classes, functions, and methods:
- `FrameExtractor`: A class responsible for extracting frames from a video file.
  - `__init__(self, video_path: str)`: Initializes the FrameExtractor object with the path to the video file.
  - `extract_frames(self) -> List[Image]`: Extracts all frames from the video file and returns them as a list of PIL Image objects.
- `GIFCreator`: A class responsible for creating a GIF from a list of frames.
  - `__init__(self, frames: List[Image], duration: float)`: Initializes the GIFCreator object with a list of frames and the desired duration (in seconds) for each frame in the final GIF.
  - `create_gif(self) -> bytes`: Creates a GIF from the frames and returns the binary data of the resulting GIF.
- `GIFRenderer`: A class responsible for rendering a large GIF from a list of smaller GIFs.
  - `__init__(self, gif_paths: List[str], num_cols: int)`: Initializes the GIFRenderer object with a list of paths to the smaller GIFs and the desired number of columns in the final GIF.
  - `render_gif(self) -> bytes`: Renders a large GIF from the smaller GIFs and returns the binary data of the resulting GIF.

entrypoint.py
