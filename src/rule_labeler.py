from typing import List

class RuleBasedNER:
    def __init__(self):
    # Price-related keywords
        self.price_keywords = ["ብር", "ክፍያ", "ዋጋ", "በ", "አነስተኛ", "ቅናሽ", "ባንኪንግ", "ነፃ", "ሽያጭ", "ግዢ", "የሚተመን", "ከ", "የሞተር", "ዋስትና"]
    # Location-related keywords
        self.location_keywords = ["አድራሻ", "ከተማ", "ገባ", "መንደር", "ወደ", "ልደታ", "ፊትለፊት", "ፕላዛ", "ሆስፒታል", "ሆቴል", "መገናኛ", "አዲስ", "ጀሞ", "ሱቅ", "አበባ", "ህንፃ", "ተኛ", "ቁጥር", "ፎቅ", "ቦሌ", "ሳሪስ", "አካባቢ", "መድሐኔዓለም", "ሜክሲኮ", "አፓርታማ", "ግራውንድ", "መሰናዶ", "ሞል", "ትቤት", "ባሉበት", "የሚገኝ", "ቅርብ", "ዞን", "ክልል", "ሰፈር",]
    # Product-related keywords
        self.product_keywords = ["ሻርታ", "ማስቀመጫ", "ባህላዊ", "አላባሽ", "ወንበር", "ዕቃ", "ልብስ", "ሹራብ", "ጫማ", "አንሶላ", "ቻርጀር", "ምቹ", "ተመራጭ", "ባትሪ", "ኳሊቲ", "መጠለያ", "መኪና", "ብርሃን", "ስጦታ", "መፍጫ", "ፍሪጅ", "ኦቭን", "ማጣሪያ", "ማንጠልጠያ", "ሴራሚክ", "መጽሐፍ", "ጋቢ", "ፔርሙስ", "ሻማ", "ትራስ", "ሞረድ", "ቢላ", "መላጫ", "መቀስ", "ፓይስትራ", "ፀጉር", "ሳሙና", "ቡና", "ዱቄት", "መዓዛ", "ሽንትቤት", "ማፅጃ", "ሽታ", "ጋዎን", "ፖን ኬክ", "ፈጢራ", "ጨጨብሳ", "ሻዋርማ", "መጠጥ", "መተኮሻ", "መጠቅለያ", "መስታዎት", "ፓትራ", "ኬክ", "ፓስታ", "ፍርኖ", "ላዛኛ", "ዘንቢል", "ጀሪካን", "ወፍራም", "አልባሳት", "ዲፕ ፍሪዝ", "ላውንደሪ", "ምድጃ", "ጎማ", "መቆለፊያ", "ቱቦ", "ቅመም"]
    def label_tokens(self, tokens: List[str]) -> List[str]:
        labels = ["O"] * len(tokens)
        i = 0

        while i < len(tokens):
            token = tokens[i]

            # --- PRICE rule ---
            if token in ["ዋጋ", "በ"] and i + 1 < len(tokens) and tokens[i + 1].isdigit():
                labels[i] = "B-PRICE"
                labels[i + 1] = "I-PRICE"
                if i + 2 < len(tokens) and tokens[i + 2] == "ብር":
                    labels[i + 2] = "I-PRICE"
                    i += 3
                    continue
                i += 2
                continue

            if token.isdigit() and i + 1 < len(tokens) and tokens[i + 1] == "ብር":
                labels[i] = "B-PRICE"
                labels[i + 1] = "I-PRICE"
                i += 2
                continue

            # --- LOCATION rule ---
            if token in self.location_keywords:
                labels[i] = "B-LOC"
                if i + 1 < len(tokens) and tokens[i + 1] in self.location_keywords:
                    labels[i + 1] = "I-LOC"
                    i += 2
                    continue
                i += 1
                continue

            # --- PRODUCT rule ---
            if token in self.product_keywords:
                labels[i] = "B-Product"
                if i + 1 < len(tokens) and tokens[i + 1] in self.product_keywords:
                    labels[i + 1] = "I-Product"
                    i += 2
                    continue
                i += 1
                continue

            i += 1

        return labels