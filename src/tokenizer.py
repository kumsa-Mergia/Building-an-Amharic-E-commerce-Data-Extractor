import re
from typing import List

class AmharicTokenizer:
    @staticmethod
    def tokenize(text: str) -> List[str]:
        # Add spaces around Amharic punctuation and common symbols
        text = re.sub(r'([፡።፣፤፥፦፧፨,!?/()«»“”"“”‘’])', r' \1 ', text)
        text = re.sub(r'\s+', ' ', text)  # Normalize spaces
        return text.strip().split()