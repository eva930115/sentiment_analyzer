import pandas as pd
import re
import os

# ✅ 使用者自訂檔案名稱（不含 .csv）
comments_title = 'test'      # YouTube_Rewind_2018
output_name = f"{comments_title}_cleaned"

# === 重點修正：設定 data/input 為根據腳本定位的資料夾 ===
script_dir = os.path.dirname(os.path.abspath(__file__))          # 取得腳本所在目錄
project_root = os.path.dirname(script_dir)                       # 根目錄（src的上一層）
data_folder = os.path.join(project_root, "data", "input")        # 專案根目錄下的 data/input

os.makedirs(data_folder, exist_ok=True)                          # 若資料夾不存在則建立

input_path = os.path.join(data_folder, f"{comments_title}.csv")
output_path = os.path.join(data_folder, f"{output_name}.csv")


# ✅ 載入原始留言檔案
df = pd.read_csv(input_path)

# ✅ 定義清理函數（移除所有標點符號）
def clean_text(text):
    if pd.isna(text):
        return ""
    text = re.sub(r"http\S+", "", text)                    # 移除網址
    text = re.sub(r"@\w+", "", text)                       # 移除 @提及
    text = re.sub(r"#\w+", "", text)                       # 移除 hashtag
    text = re.sub(r"[^\w\s]", "", text)                    # ✅ 移除所有標點符號（含逗號）
    text = re.sub(r"[\u2000-\u2BFF\uFE00-\uFEFF]", "", text)  # 移除特殊 Unicode 字元
    text = re.sub(r"\s+", " ", text)                       # 多個空白合併
    return text.strip()

# ✅ 套用清理函數
df["clean_text"] = df["text"].apply(clean_text)

# ✅ 移除空白留言
df = df[df["clean_text"].str.strip() != ""]

# ✅ 每行加上逗號，最後一行不加
cleaned_lines = df["clean_text"].tolist()
cleaned_lines_with_commas = [line + "," for line in cleaned_lines[:-1]] + [cleaned_lines[-1]]

# ✅ 儲存為每行一留言的 csv（純文字形式）
with open(output_path, "w", encoding="utf-8-sig") as f:
    for line in cleaned_lines_with_commas:
        f.write(line + "\n")

# ✅ 顯示資訊
print(f"📁 已清理並儲存 {len(cleaned_lines)} 則留言，每則留言一行，檔案位置：{output_path}")
