````markdown
## 🔠 Amharic Named Entity Recognition (NER) – Fine-Tuned Model

This repository includes a fine-tuned Named Entity Recognition (NER) model for the Amharic language. The model was trained on labeled Telegram e-commerce data using the Hugging Face `transformers` library.

### 🧠 Model Overview

- **Language**: Amharic (`am`)
- **Model type**: Token Classification (NER)
- **Base model**: `Davlan/bert-base-amharic`
- **Entities Recognized**:
  - `Product`
  - `Price`
  - `Location`

### 📁 Model Files

Due to GitHub's file size restrictions, the trained model is not stored directly in this repository.

### 🔗 Download Model

You can download the fine-tuned model from the following Google Drive link:

👉 [Download Amharic NER Model (ZIP, ~766MB)](https://drive.google.com/drive/folders/1_nYhtvLlBe2P8tq5-rOsu-VFGBifQURW?usp=drive_link)

> Once downloaded, extract the ZIP file and load the model using `transformers`:

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

model_dir = "path_to_extracted_model_folder"
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForTokenClassification.from_pretrained(model_dir)
```
````

---

### 📊 Training Details

- **Epochs**: 10
- **Evaluation Metrics**: Precision, Recall, F1 Score per entity
- **Framework**: Hugging Face Transformers, PyTorch

---

### 📌 Acknowledgments

- Base model: [`Davlan/bert-base-amharic`](https://huggingface.co/Davlan/bert-base-amharic)
- Data Source: Telegram e-commerce messages

---

### 📂 Related Files

- `Fine-Tune/Amharic_NER_FineTuning.ipynb`: Training notebook
- `Data/`: Contains cleaned and preprocessed data
- `amharic-ner-model.zip`: [Download from Google Drive]([https://drive.google.com/your-shared-link-here](https://drive.google.com/drive/folders/1_nYhtvLlBe2P8tq5-rOsu-VFGBifQURW?usp=drive_link))

```

```
