## 🔠 Amharic Named Entity Recognition (NER) – Fine-Tuned Model

This repository hosts a fine-tuned Named Entity Recognition (NER) model for the **Amharic** language, trained on Telegram-based e-commerce messages using Hugging Face `transformers`.

### 🧠 Model Overview

- **Language**: Amharic (`am`)
- **Model Type**: Token Classification (NER)
- **Base Model**: [`Davlan/bert-base-amharic`](https://huggingface.co/Davlan/bert-base-amharic)
- **Entities Recognized**:
  - `Product`
  - `Price`
  - `Location`

---

### 📁 Model Access

Due to GitHub's file size restrictions, the trained model files are hosted externally.

👉 **[amharic-ner-model](https://drive.google.com/drive/folders/1_nYhtvLlBe2P8tq5-rOsu-VFGBifQURW?usp=drive_link)**

> You can clone or download the entire folder from Google Drive. The directory contains all necessary files for loading the model and tokenizer.

---

### 💡 How to Load the Model

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification

model_path = "path/to/amharic-ner-model"  # Replace with your actual path
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForTokenClassification.from_pretrained(model_path)
````

---

### 📊 Training Details

* **Epochs**: 10
* **Metrics Tracked**:

  * Precision, Recall, F1 Score (per entity type)
  * Overall Accuracy
* **Frameworks**: Hugging Face Transformers, PyTorch

---

### 📂 Repository Contents

* `Fine-Tune/Amharic_NER_FineTuning.ipynb` – Model training notebook
* `Data/` – Cleaned and preprocessed Telegram e-commerce messages
* `amharic-ner-model/` – Folder containing trained model and tokenizer files

---

### 🙏 Acknowledgments

* Base Model: [`Davlan/bert-base-amharic`](https://huggingface.co/Davlan/bert-base-amharic)
* Data Source: Public Telegram channels related to Ethiopian e-commerce

---


