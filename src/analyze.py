# analyze.py

import pandas as pd
import joblib
import matplotlib.pyplot as plt
import sys
import re
from collections import Counter

# 文字清理函數（與訓練時一致）
def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#\w+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.lower().strip()

# 1. 載入模型與向量器
clf = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# 2. 讀取輸入留言檔（CSV 檔，須含欄位 'text'）
input_file = sys.argv[1] if len(sys.argv) > 1 else "data/input_comments.csv"
df = pd.read_csv(input_file)

# 3. 清理留言文字
df["text_clean"] = df["text"].apply(clean_text)

# 4. 向量化並預測情緒
X = vectorizer.transform(df["text_clean"])
df["predicted"] = clf.predict(X)

# 5. 儲存結果為 result.csv
df.to_csv("outputs/result.csv", index=False)
print("✅ 已輸出 result.csv")

# 6. 統計情緒比例
count = Counter(df["predicted"])
labels = ["Negative", "Positive"]
sizes = [count.get(0, 0), count.get(1, 0)]

# 7. 繪製圓餅圖
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.axis("equal")
plt.title("Sentiment Distribution")
plt.savefig("outputs/pie_chart.png")
plt.show()

# 8. 繪製長條圖
import numpy as np

plt.figure(figsize=(6, 4))
bars = plt.bar(["Negative", "Positive"], sizes)

# 在長條上方加上數字標籤
for i, v in enumerate(sizes):
    plt.text(i, v + 1, str(v), ha='center', va='bottom')

plt.ylabel("Number of Comments")
plt.title("Sentiment Classification Count")
plt.savefig("outputs/bar_chart.png")
plt.show()
