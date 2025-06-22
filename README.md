# 💬 Sentiment Analyzer 情緒分類系統

這是一個使用 Python 與機器學習技術建構的留言情緒分析工具，能夠自動判斷留言屬於正向還是負向，並輸出結果與圖表分析。

---

## 📁 專案結構

```text
sentiment_analyzer/
├── data/                                 # 📂 所有資料集相關檔案(檔案太大無法上傳)
│   ├── raw/                              # 原始資料（尚未清理）
│   │   ├── training.1600000.processed.noemoticon.csv    # Sentiment140 原始檔（Kaggle 下載）
│   │   ├── twitter_training.csv    # 測試集資料
│   │   └── clean_training.py       # 清理測試集資料
│   ├── processed/                        # 處理後可直接訓練使用的資料集
│   │   ├── sentiment140_clean.csv     # 英文資料清理後版本
│   │   ├── chnsenti_clean.csv         # 中文資料（ChnSentiCorp）清理後版本
│   │   ├── combined_multilang.csv     # 中英文合併後的資料集
│   │   └── cleaned_sentiment_training.csv   # 清理後的測試集資料
│   └── input/                            # 使用者輸入的影片留言檔案（可自定義）
│       ├── YouTube_Rewind_2018.csv
│       ├── YouTube_Rewind_2018_cleaned.csv
│       ├── CES_2025_Keynote.csv
│       ├── CES_2025_Keynote_cleaned.csv
│       ├── test.csv
│       └── test_cleaned.csv
│
├── models/                               # 📂 訓練產生的模型與向量器(檔案太大無法上傳)
│   └── bert_multilang/                   # 使用 BERT multilingual 訓練出的模型
│       ├── config.json
│       ├── model.safetensors
│       ├── special_tokens_map.json
│       ├── tokenizer_config.json
│       ├── training_args.bin
│       └── vocab.txt
│
├── outputs/                              # 📂 輸出結果（圖表、報表）
│   ├── YouTube_Rewind_2018.png
│   ├── CES_2025_Keynote.png
│   └── test.png
│
├── src/                                  # 📂 所有 Python 腳本
│   ├── preproccess.ipynb                 # 資料清理與轉換的 Jupyter Notebook
│   ├── train_multilingual_bert.ipynb     # 使用 transformers 訓練 BERT 模型
│   ├── comment_catch.py                  # 擷取指定 YouTube 留言影片
│   ├── comment_clean.py                  # 清理留言文字（簡繁轉換、符號清除等）
│   ├── analyze.py                        # 分析留言並輸出情緒結果
│   ├── evaluate.py                       # 評估模型表現
│   ├── pie_chart_generator.py            # 產生圓餅圖
│   └── test.py                           # 測試用腳本
│
├── app/                                  # 📂 使用者應用
│   └── app.py                            # 主執行介面，用戶輸入影片網址並取得分析
│
├── requirements.txt                      # 📄 Python 套件需求清單
└── README.md                             # 📄 專案說明文件
```

---

## 🚀 安裝與環境建置

1.  建立虛擬環境並啟用：

    ```bash
    python -m venv venv  
    venv\Scripts\activate         # Windows
    source venv/bin/activate       # macOS/Linux
    ```

2.  安裝套件：

    ```bash
    pip install -r requirements.txt
    ```

---

## 📦 requirements.txt 內容

```text
altair==5.5.0
attrs==25.3.0
blinker==1.9.0
cachetools==5.5.2
certifi==2025.4.26
charset-normalizer==3.4.2
click==8.2.1
colorama==0.4.6
contourpy==1.3.2
cycler==0.12.1
filelock==3.18.0
fonttools==4.58.4
fsspec==2025.5.1
gitdb==4.0.12
GitPython==3.1.44
google-api-core==2.25.1
google-api-python-client==2.173.0
google-auth==2.40.3
google-auth-httplib2==0.2.0
googleapis-common-protos==1.70.0
httplib2==0.22.0
huggingface-hub==0.33.0
idna==3.10
Jinja2==3.1.6
joblib==1.5.1
jsonschema==4.24.0
jsonschema-specifications==2025.4.1
kiwisolver==1.4.8
MarkupSafe==3.0.2
matplotlib==3.10.3
mpmath==1.3.0
narwhals==1.42.0
networkx==3.5
numpy==2.3.0
packaging==24.2
pandas==2.3.0
pillow==11.2.1
proto-plus==1.26.1
protobuf==6.31.1
pyarrow==20.0.0
pyasn1==0.6.1
pyasn1_modules==0.4.2
pydeck==0.9.1
pyparsing==3.2.3
python-dateutil==2.9.0.post0
pytz==2025.2
PyYAML==6.0.2
referencing==0.36.2
regex==2024.11.6
requests==2.32.4
rpds-py==0.25.1
rsa==4.9.1
safetensors==0.5.3
scikit-learn==1.7.0
scipy==1.15.3
six==1.17.0
smmap==5.0.2
streamlit==1.45.1
sympy==1.14.0
tenacity==9.1.2
threadpoolctl==3.6.0
tokenizers==0.21.1
toml==0.10.2
torch==2.7.1+cu118
torchaudio==2.7.1+cu118
torchvision==0.22.1+cu118
tornado==6.5.1
tqdm==4.67.1
transformers==4.52.4
typing_extensions==4.14.0
tzdata==2025.2
uritemplate==4.2.0
urllib3==2.4.0
watchdog==6.0.0
```

---

## 📖 使用流程

本專案主要包含以下幾個流程，請依序執行 Jupyter Notebooks 或 Python 腳本：

1.  **資料前處理**: 執行 `src/preproccess.ipynb` 來清理與準備訓練資料。
2.  **模型訓練**: 執行 `src/train_multilingual_bert.ipynb` 來訓練多語言 BERT 模型。
3.  **留言擷取**: 執行 `src/comment_catch.py` 來從指定的 YouTube 影片擷取留言。
4.  **留言清理**: 執行 `src/comment_clean.py` 來清理擷取到的留言。
5.  **情緒分析**: 執行 `src/analyze.py` 來分析清理後的留言，並將結果輸出。
6.  **圖表產生**: 執行 `src/pie_chart_generator.py` 來產生情緒分析結果的圖表。
7.  **應用程式**: 執行 `app/app.py` 啟動 Streamlit 應用程式，提供使用者互動介面。

**使用方式**

輸入以下指令開啟網頁進行測試
```
streamlit run app/app.py 
```

---

## 🧠 授權與說明

本專案僅供教學與學術研究用途，資料來自 Kaggle 的 [Sentiment140 Dataset](https://www.kaggle.com/datasets/kazanova/sentiment140)。

作者：資工三 111590013 呂念庭、資工三 111590056 王逸婕