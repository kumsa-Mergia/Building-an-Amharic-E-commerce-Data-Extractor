import pandas as pd
import re

class AmharicDataCleaner:
    def __init__(self, min_length: int = 10, require_amharic: bool = True):
        self.min_length = min_length
        self.require_amharic = require_amharic

    def is_amharic(self, text: str) -> bool:
        return bool(re.search(r'[\u1200-\u137F]', text))

    def clean_dataframe(self, df: pd.DataFrame, text_col: str = "text") -> pd.DataFrame:
        df = df.copy()  # <-- Ensure we are working on a copy
        
        df = df.dropna(subset=[text_col])
        df[text_col] = df[text_col].astype(str).str.strip()
        df = df[df[text_col].str.len() > self.min_length]
        df = df.drop_duplicates(subset=[text_col])

        if self.require_amharic:
            df = df[df[text_col].apply(self.is_amharic)]

        return df.reset_index(drop=True)
