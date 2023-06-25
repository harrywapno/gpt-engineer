import cv2
import os

class GifGenerator:
    def __init__(self):
        pass

    def generate_gifs(self, input_path: str, output_folder: str):
        cap = cv2.VideoCapture(input_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for i in range(0, frame_count, 42):
            cap.set(cv2.CAP_PROP_POS_FRAMES, i)
            ret, frame = cap.read()
            if not ret:
                break

            output_path = os.path.join(output_folder, f'{i}.gif')
            cv2.imwrite(output_path, frame)

        cap.release()
