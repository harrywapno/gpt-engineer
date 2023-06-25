class TextFileWriter:
    def __init__(self, text_file_path: str):
        self.text_file_path = text_file_path

    def write_text_to_file(self, text: str):
        with open(self.text_file_path, 'w', encoding='utf-8') as f:
            f.write(text)
