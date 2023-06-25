import cv2
import numpy as np
import tensorflow as tf

class VideoColorizer:
    def __init__(self, model_path: str):
        self.model = tf.keras.models.load_model(model_path)

    def colorize_video(self, input_path: str, output_path: str):
        cap = cv2.VideoCapture(input_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.resize(frame, (256, 256))
            frame = np.expand_dims(frame, axis=-1)
            frame = np.expand_dims(frame, axis=0)
            frame = frame / 255.0

            colorized_frame = self.model.predict(frame)
            colorized_frame = np.squeeze(colorized_frame, axis=0)
            colorized_frame = np.clip(colorized_frame, 0, 1)
            colorized_frame = cv2.cvtColor(colorized_frame, cv2.COLOR_RGB2BGR)
            colorized_frame = cv2.resize(colorized_frame, (width, height))

            out.write(colorized_frame)

        cap.release()
        out.release()
        cv2.destroyAllWindows()
