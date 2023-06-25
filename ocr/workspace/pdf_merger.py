from PyPDF2 import PdfFileMerger
from typing import List


class PDFMerger:
    def __init__(self, pdf_paths: List[str]):
        self.pdf_paths = pdf_paths

    def merge(self, output_path: str) -> str:
        merger = PdfFileMerger()
        for pdf_path in self.pdf_paths:
            merger.append(pdf_path)
        merger.write(output_path)
        merger.close()
        return output_path
