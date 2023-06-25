from movie import Movie
from pydub import AudioSegment
from audio import Audio

def isolate_audio(movie: Movie) -> Audio:
    # Load movie audio
    movie_audio = AudioSegment.from_file(movie.file_path)

    # Isolate audio
    # ...

    # Save audio file
    # ...

    # Create Audio object
    audio = Audio(title=movie.title, file_path=audio_file_path)

    return audio
