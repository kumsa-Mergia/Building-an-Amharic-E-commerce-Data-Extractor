from typing import List

class CoNLLLabeler:
    def __init__(self):
        self.labeled_blocks = []

    def to_conll_block(self, tokens: List[str], labels: List[str]) -> str:
        assert len(tokens) == len(labels), "Token and label lengths must match"
        block = "\n".join([f"{tok} {label}" for tok, label in zip(tokens, labels)])
        return block + "\n\n"

    def add_labeled_message(self, tokens: List[str], labels: List[str]):
        block = self.to_conll_block(tokens, labels)
        self.labeled_blocks.append(block)

    def save_to_file(self, filepath: str):
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(self.labeled_blocks)