from typing import List
from PIL import Image
import cv2

class FrameExtractor:
    def __init__(self, video_path: str):
        self.video_path = video_path

    def extract_frames(self) -> List[Image]:
        frames = []
        cap = cv2.VideoCapture(self.video_path)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            frames.append(frame)
        cap.release()
        return frames
