import re

import nltk
from nltk.corpus import stopwords

nltk.download("stopwords", quiet=True)
stop_words = set(stopwords.words("english"))


def preprocess_text(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as input_file:
        input_text = input_file.read()

    text = re.sub(r"[\n\r]+", "\n", input_text)
    text = re.sub(r"[^a-zA-Z0-9\s_.,!?:;@#$%^&*()+\-=[\]{}|\\<>`~'\"/]+", "", text)
    text = re.sub(r"\s+", " ", text)
    text = text.lower()

    words = text.split()
    words = [word for word in words if word not in stop_words]
    text = " ".join(words)

    with open(output_file, "w", encoding="utf-8") as output_file:
        output_file.write(text.strip())
