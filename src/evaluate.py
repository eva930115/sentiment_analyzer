# sentiment_analyzer/src/evaluate.py
import os
import pandas as pd
from transformers import pipeline
from sklearn.metrics import classification_report
import torch
from tqdm import tqdm  # <-- 新增

def evaluate_model(comments_title: str):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    data_path = os.path.join(project_root, "data", "processed", "cleaned_sentiment_training.csv")
    df = pd.read_csv(data_path)
    if 'text' not in df.columns or 'label' not in df.columns:
        raise ValueError("CSV 檔案中必須包含 'text' 與 'label' 欄位。")

    # 保證 text 跟 label 都不是 NaN，索引對齊
    df = df.dropna(subset=["text", "label"])
    texts = df["text"].astype(str).tolist()
    true_labels = df["label"].tolist()


    model_dir = os.path.join(project_root, "models", "bert_multilang")
    sentiment_pipeline = pipeline(
        "text-classification",
        model=model_dir,
        tokenizer=model_dir,
        device=0 if torch.cuda.is_available() else -1
    )

    # === 加上 tqdm 跑條 ===
    batch_size = 32  # 或更小，依你顯卡/CPU 決定
    pred_labels = []
    for i in tqdm(range(0, len(texts), batch_size), desc="模型預測中"):
        batch = texts[i:i+batch_size]
        preds = sentiment_pipeline(batch, truncation=True, padding=True)
        pred_labels.extend([1 if p['label'].lower() == 'positive' else 0 for p in preds])

    print("\n=== 評估報告 ===")
    print(classification_report(true_labels, pred_labels, digits=4))

if __name__ == "__main__":
    evaluate_model("test")  # 替換為你的 comments_title
