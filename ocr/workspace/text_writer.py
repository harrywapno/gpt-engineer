class TextWriter:
    def __init__(self, output_file_path: str):
        self.output_file_path = output_file_path

    def write(self, text: str):
        with open(self.output_file_path, 'w', encoding='utf-8') as f:
            f.write(text)
