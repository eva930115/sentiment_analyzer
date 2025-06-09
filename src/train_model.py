# src/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
import os

# 資料路徑
input_path = "data/processed/sentiment140_clean.csv"
model_path = "models/model.pkl"
vectorizer_path = "models/vectorizer.pkl"

# 建立 models 資料夾（若尚未存在）
os.makedirs("models", exist_ok=True)

# 1. 載入資料
print("📂 載入資料中...")
df = pd.read_csv(input_path)
texts = df["text"]
labels = df["target"]

# 2. 切分訓練集與測試集
print("🔄 切分訓練集與測試集...")
X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

# 3. 文本向量化：TF-IDF
print("🔠 向量化文字資料 (TF-IDF)...")
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
print("✅ 向量化完成")

# 4. 建立與訓練模型
print("🔧 開始訓練模型（Logistic Regression）...")
clf = LogisticRegression(max_iter=1000, verbose=1)  # verbose 顯示進度
clf.fit(X_train_vec, y_train)
print("✅ 模型訓練完成")

# 5. 預測與評估
print("📊 模型評估報告：")
y_pred = clf.predict(X_test_vec)
print(classification_report(y_test, y_pred))

# 6. 儲存模型與向量器
print("💾 儲存模型與向量器...")
joblib.dump(clf, model_path)
joblib.dump(vectorizer, vectorizer_path)
print(f"✅ 模型儲存完成：{model_path}")
print(f"✅ 向量器儲存完成：{vectorizer_path}")
