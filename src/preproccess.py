# src/preprocess.py

import pandas as pd
import re
import os

# 1. 指定欄位名稱（Sentiment140 原始欄位）
columns = ["target", "ids", "date", "flag", "user", "text"]

# 2. 讀取原始檔案（指定編碼 ISO-8859-1）
input_path = "data/raw/training.1600000.processed.noemoticon.csv"
df = pd.read_csv(input_path, encoding="ISO-8859-1", names=columns)
print(df)

# # 3. 只保留必要欄位
# df = df[["text", "target"]]

# # 4. 把 4（正向）轉為 1，0（負向）保持不變
# df["target"] = df["target"].apply(lambda x: 1 if x == 4 else 0)

# # 5. 定義清理函式
# def clean_text(text):
#     text = re.sub(r"http\S+", "", text)      # 移除網址
#     text = re.sub(r"@\w+", "", text)         # 移除提及
#     text = re.sub(r"#\w+", "", text)         # 移除 hashtag
#     text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # 移除特殊字元
#     return text.lower().strip()

# # 6. 清理留言內容
# df["text"] = df["text"].astype(str).apply(clean_text)

# # 7. 移除空白或重複留言
# df = df[df["text"] != ""]
# df = df.drop_duplicates(subset="text")

# # 8. 建立輸出資料夾
# output_dir = "data/processed"
# os.makedirs(output_dir, exist_ok=True)

# # 9. 輸出清理後資料
# output_path = os.path.join(output_dir, "sentiment140_clean.csv")
# df.to_csv(output_path, index=False)

# print(f"✅ 已完成前處理，儲存於：{output_path}")
# print(f"👉 共 {len(df)} 筆資料")
