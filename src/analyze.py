import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification, pipeline
import torch
import os
import sys

def analyze_sentiment(comments_title):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_path = os.path.join(project_root, "data", "input", f"{comments_title}_cleaned.csv")
    df = pd.read_csv(data_path, header=None, names=["text"])

    if 'text' not in df.columns:
        raise ValueError("The input CSV must contain a 'text' column.")

    model_dir = os.path.join(project_root, "models", "bert_multilang")
    tokenizer = BertTokenizer.from_pretrained(model_dir)
    model = BertForSequenceClassification.from_pretrained(model_dir)
    sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

    texts = df['text'].dropna().astype(str).tolist()
    results = sentiment_pipeline(texts, truncation=True, padding=True)

    sentiment_counts = {'POSITIVE': 0, 'NEGATIVE': 0}
    for result in results:
        label = result['label'].upper()
        if label in sentiment_counts:
            sentiment_counts[label] += 1

    return sentiment_counts

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        comments_title = sys.argv[1]
    else:
        comments_title = 'test'
    result = analyze_sentiment(comments_title)
    print(result)
