# 💬 Sentiment Analyzer 情緒分類系統

這是一個使用 Python 與機器學習技術建構的留言情緒分析工具，能夠自動判斷留言屬於正向還是負向，並輸出結果與圖表分析。

---

## 📁 專案結構

```text
sentiment_analyzer/
├── data/
│   ├── raw/                    # 原始資料 (Kaggle下載)  (檔案太大無法上傳)
│   │   └── training.1600000.processed.noemoticon.csv
│   ├── processed/              # 前處理完的資料   (檔案太大無法上傳)
│   │   └── sentiment140_clean.csv
│   └── input/                  # 使用者提供的留言 CSV
│       └── input_comments.csv
├── models/                     # 訓練後的模型與向量器
│   ├── model.pkl
│   └── vectorizer.pkl
├── outputs/                    # 預測結果與圖表
│   ├── result.csv
│   ├── pie_chart.png
│   └── bar_chart.png
├── src/                        # 所有 Python 執行腳本
│   ├── preprocess.py           # 前處理原始資料
│   ├── train_model.py          # 訓練模型 (含進度訊息)
│   └── analyze.py              # 分析留言並輸出結果與圖表
├── requirements.txt            # 所需套件清單
└── README.md                   # 專案說明文件
```

---

## 🚀 安裝與環境建置

1. 建立虛擬環境並啟用：

   ```bash
   python -m venv venv  
   venv\Scripts\activate         # Windows
   source venv/bin/activate       # macOS/Linux
   ```

2. 安裝套件：

   ```bash
   pip install -r requirements.txt
   ```

---

## 📦 requirements.txt 內容

```text
pandas
scikit-learn
matplotlib
joblib
```

---

## 🧹 第 1 步：前處理資料

將原始的 Sentiment140 檔案放在 `data/raw/` 資料夾內，執行：

```bash
python src/preprocess.py
```

輸出檔案： `data/processed/sentiment140_clean.csv`

---

## 🏋️ 第 2 步：訓練模型

```bash
python src/train_model.py
```

訓練後模型與向量器輸出到：

* `models/model.pkl`
* `models/vectorizer.pkl`

---

## ✨ 第 3 步：分析留言資料

將要分析的留言 CSV (需包含欄位 `text`) 放至 `data/input/`，例如：

```
data/input/input_comments.csv
```

執行：

```bash
python src/analyze.py data/input/input_comments.csv
```

輸出檔案：

* `outputs/result.csv`      # 包含每筆留言與預測標籤、信心分數
* `outputs/pie_chart.png`   # 情緒比例圓餅圖
* `outputs/bar_chart.png`   # 正負面數量長條圖

---

## 📌 注意事項

* 本模型使用英文推文訓練，若要分析中文留言，建議先準備中文語料再行訓練。
* 請確保 `input_comments.csv` 第一行為 `text` 標題，且每行只有一則留言。

---

## 🧠 授權與說明

本專案僅供教學與學術研究用途，資料來自 Kaggle 的 [Sentiment140 Dataset](https://www.kaggle.com/datasets/kazanova/sentiment140)。

作者：資工三 111590013 呂念庭、資工三 111590056 王逸婕