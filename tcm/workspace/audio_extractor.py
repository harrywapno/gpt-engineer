import moviepy.editor as mp

class AudioExtractor:
    def __init__(self):
        pass

    def extract_audio(self, input_path: str, output_path: str):
        video = mp.VideoFileClip(input_path)
        audio = video.audio
        audio.write_audiofile(output_path)
