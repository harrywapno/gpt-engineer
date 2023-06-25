import re

class TextCleaner:
    def __init__(self):
        pass
    
    def clean_text(self, text: str) -> str:
        """
        Cleans up the plain text output
        """
        # Remove non-alphanumeric characters
        text = re.sub(r"[^a-zA-Z0-9ąćęłńóśźżĄĆĘŁŃÓŚŹŻ\s]+", "", text)
        
        # Remove extra whitespace
        text = re.sub(r"\s+", " ", text)
        text = text.strip()
        
        return text
