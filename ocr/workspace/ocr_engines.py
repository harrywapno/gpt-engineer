from abc import ABC, abstractmethod

class OCR(ABC):
    @abstractmethod
    def recognize(self, file_path: str) -> str:
        pass
