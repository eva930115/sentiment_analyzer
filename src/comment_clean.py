import pandas as pd
import re
import os
import sys

# CLI 參數處理
if len(sys.argv) >= 2:
    comments_title = sys.argv[1]
else:
    comments_title = 'test'

output_name = f"{comments_title}_cleaned"

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
data_folder = os.path.join(project_root, "data", "input")
os.makedirs(data_folder, exist_ok=True)

input_path = os.path.join(data_folder, f"{comments_title}.csv")
output_path = os.path.join(data_folder, f"{output_name}.csv")

df = pd.read_csv(input_path)

def clean_text(text):
    if pd.isna(text):
        return ""
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#\w+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"[\u2000-\u2BFF\uFE00-\uFEFF]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

df["clean_text"] = df["text"].apply(clean_text)
df = df[df["clean_text"].str.strip() != ""]

cleaned_lines = df["clean_text"].tolist()
if cleaned_lines:
    cleaned_lines_with_commas = [line + "," for line in cleaned_lines[:-1]] + [cleaned_lines[-1]]
else:
    cleaned_lines_with_commas = []

with open(output_path, "w", encoding="utf-8-sig") as f:
    for line in cleaned_lines_with_commas:
        f.write(line + "\n")

print(f"📁 已清理並儲存 {len(cleaned_lines)} 則留言，每則留言一行，檔案位置：{output_path}")
