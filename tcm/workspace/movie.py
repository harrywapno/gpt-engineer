from dataclasses import dataclass

@dataclass
class Movie:
    title: str
    file_path: str
    colorized: bool = False
