from typing import List
from PIL import Image
from frame_extractor import FrameExtractor
from gif_creator import GIFCreator
from gif_renderer import GIFRenderer

VIDEO_PATH = "path/to/video.mp4"
NUM_FRAMES_PER_GIF = 42
FINAL_GIF_NUM_COLS = 5
FINAL_GIF_DURATION = 12

if __name__ == "__main__":
    # Extract frames from video
    frame_extractor = FrameExtractor(VIDEO_PATH)
    frames = frame_extractor.extract_frames()

    # Create GIFs from frames
    num_frames = len(frames)
    num_gifs = (num_frames // NUM_FRAMES_PER_GIF) + 1
    gif_paths = []
    for i in range(num_gifs):
        start_idx = i * NUM_FRAMES_PER_GIF
        end_idx = min((i + 1) * NUM_FRAMES_PER_GIF, num_frames)
        gif_creator = GIFCreator(frames[start_idx:end_idx], FINAL_GIF_DURATION / NUM_FRAMES_PER_GIF)
        gif_data = gif_creator.create_gif()
        gif_path = f"gif_{i}.gif"
        with open(gif_path, "wb") as f:
            f.write(gif_data)
        gif_paths.append(gif_path)

    # Render final GIF from smaller GIFs
    gif_renderer = GIFRenderer(gif_paths, FINAL_GIF_NUM_COLS)
    final_gif_data = gif_renderer.render_gif()
    with open("final.gif", "wb") as f:
        f.write(final_gif_data)
