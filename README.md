# 📦 Building-an-Amharic-E-commerce-Data-Extractor

This project builds an end-to-end pipeline to **scrape, preprocess, label, train, interpret, and apply NER models** on **Amharic e-commerce messages** from Telegram. The goal is to extract key entities like `Product`, `Price`, and `Location`, and use them to generate vendor insights for micro-lending.

* Scrape messages (text, images, docs) from **6 Ethiopian Telegram e-commerce channels**.
* Clean and preprocess Amharic text: tokenize, normalize, and extract metadata.
* Store in structured format (e.g., CSV or JSON).

### : Dataset Labeling (CoNLL Format)
### : NER Model Fine-Tuning
### : Model Comparison & Selection
### : Model Interpretability

## 🔧 Requirements

* Python 3.8+
* `telethon`, `pandas`, `transformers`, `datasets`, `scikit-learn`, `shap`, `lime`
* `.env` with Telegram API credentials
* GPU for model training (Colab or local)

---

## 🚀 Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/kumsa-Mergia/Building-an-Amharic-E-commerce-Data-Extractor.git
   cd Building-an-Amharic-E-commerce-Data-Extractor
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Add your `.env` file with Telegram API credentials:

   ```
   API_ID=your_api_id
   API_HASH=your_api_hash
   PHONE=your_phone
   ```

4. Run the scraper:

   ```bash
   python scripts/scraper.py
   ```

---

## 👥 Contributing

* Share labeled datasets for collaborative fine-tuning.



