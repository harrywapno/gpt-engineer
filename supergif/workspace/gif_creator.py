from typing import List
from PIL import Image
import imageio
from dataclasses import dataclass

@dataclass
class FrameData:
    image: Image
    duration: float

class GIFCreator:
    def __init__(self, frames: List[Image], duration: float):
        self.frames = frames
        self.duration = duration

    def create_gif(self) -> bytes:
        frame_data = [FrameData(frame, self.duration) for frame in self.frames]
        with imageio.get_writer("temp.gif", mode="I", duration=self.duration) as writer:
            for data in frame_data:
                writer.append_data(data.image)
        with open("temp.gif", "rb") as f:
            gif_data = f.read()
        return gif_data
