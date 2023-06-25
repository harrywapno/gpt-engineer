from typing import List
import imageio
from PIL import Image
from dataclasses import dataclass

@dataclass
class GIFData:
    path: str
    duration: float

class GIFRenderer:
    def __init__(self, gif_paths: List[str], num_cols: int):
        self.gif_paths = gif_paths
        self.num_cols = num_cols

    def render_gif(self) -> bytes:
        gif_data = [GIFData(path, self.get_gif_duration(path)) for path in self.gif_paths]
        num_gifs = len(gif_data)
        num_rows = (num_gifs // self.num_cols) + 1
        max_duration = max([data.duration for data in gif_data])
        with imageio.get_writer("temp.gif", mode="I", duration=max_duration) as writer:
            for i, data in enumerate(gif_data):
                row_idx = i // self.num_cols
                col_idx = i % self.num_cols
                with imageio.get_reader(data.path) as reader:
                    for frame in reader:
                        writer.append_data(frame)
                if col_idx == self.num_cols - 1:
                    for _ in range(row_idx + 1, num_rows):
                        writer.append_data(Image.new("RGB", reader.get_data(0).shape[:2], (255, 255, 255)))
        with open("temp.gif", "rb") as f:
            final_gif_data = f.read()
        return final_gif_data

    def get_gif_duration(self, path: str) -> float:
        with imageio.get_reader(path) as reader:
            return reader.get_meta_data()["duration"] / 1000.0
