import pandas as pd
from transformers import BertTokenizer, BertForSequenceClassification, pipeline
import torch
import os

def analyze_sentiment(comments_title):
    # Step 1: Load cleaned data
    # 取得目前腳本所在目錄（src 資料夾）
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 專案根目錄（sentiment_analyzer）
    project_root = os.path.dirname(script_dir)
    # 建立 input 資料的完整路徑
    data_path = os.path.join(project_root, "data", "input", f"{comments_title}_cleaned.csv")
    df = pd.read_csv(data_path, header=None, names=["text"])

    if 'text' not in df.columns:
        raise ValueError("The input CSV must contain a 'text' column.")

    # Step 2: Load model and tokenizer
    model_dir = os.path.join(project_root, "models", "bert_multilang")
    tokenizer = BertTokenizer.from_pretrained(model_dir)
    model = BertForSequenceClassification.from_pretrained(model_dir)

  
    # Step 3: Create sentiment analysis pipeline
    sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

    # Step 4: Perform prediction
    texts = df['text'].dropna().astype(str).tolist()
    results = sentiment_pipeline(texts, truncation=True, padding=True)
    # results = sentiment_pipeline(df['text'].tolist(), truncation=True, padding=True)

    # Step 5: Count sentiments
    sentiment_counts = {'POSITIVE': 0, 'NEGATIVE': 0}
    for result in results:
        label = result['label'].upper()
        if label in sentiment_counts:
            sentiment_counts[label] += 1

    return sentiment_counts    # sentiment_counts

# Example:
comments_title = 'test'      # YouTube_Rewind_2018
result = analyze_sentiment(f"{comments_title}")
print(result)
