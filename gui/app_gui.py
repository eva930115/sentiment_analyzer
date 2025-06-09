# gui/app_gui.py

import tkinter as tk
from tkinter import messagebox
import joblib
import re

# 載入模型與向量器
clf = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# 清理函數
def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#\w+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text.lower().strip()

# 分析函數
def analyze():
    raw = entry.get("1.0", tk.END).strip()
    if not raw:
        messagebox.showwarning("輸入錯誤", "請輸入留言文字")
        return

    clean = clean_text(raw)
    X = vectorizer.transform([clean])
    pred = clf.predict(X)[0]
    proba = clf.predict_proba(X)[0]

    sentiment = "😊 正向" if pred == 1 else "😠 負向"
    result_label.config(text=f"結果：{sentiment}")
    confidence_label.config(text=f"信心：正向 {proba[1]:.2f}｜負向 {proba[0]:.2f}")

# 建立視窗
window = tk.Tk()
window.title("情緒分析器")
window.geometry("400x300")

# 元件
tk.Label(window, text="請輸入留言：").pack(pady=5)
entry = tk.Text(window, height=5, width=45)
entry.pack()

tk.Button(window, text="分析", command=analyze).pack(pady=10)
result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack()

confidence_label = tk.Label(window, text="", font=("Arial", 10))
confidence_label.pack()

window.mainloop()
