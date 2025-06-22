import streamlit as st
import os
import sys
import subprocess
import re

# 取得專案根目錄
app_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(app_dir)
src_dir = os.path.join(project_root, "src")
data_input_dir = os.path.join(project_root, "data", "input")
outputs_dir = os.path.join(project_root, "outputs")

# 解析 YouTube 影片 ID
def extract_video_id(url):
    # 支援多種 youtube 連結格式
    patterns = [
        r"youtu\.be/([^?&]+)",
        r"youtube\.com/watch\?v=([^?&]+)",
        r"youtube\.com/embed/([^?&]+)"
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

st.title("YouTube 留言情感分析小工具")

youtube_url = st.text_input("請輸入 YouTube 影片連結")
comments_title = st.text_input("請輸入影片名稱（檔案名用，不含副檔名）")

if st.button("開始分析"):
    if not youtube_url or not comments_title:
        st.warning("請填寫所有欄位")
        st.stop()

    # 1. 解析影片ID
    video_id = extract_video_id(youtube_url)
    if not video_id:
        st.error("無法從連結解析影片 ID，請確認連結格式正確！")
        st.stop()
    st.info(f"影片 ID 解析為：{video_id}")

    # 2. 執行 comment_catch.py 取得留言
    st.write("抓取 YouTube 留言中...")
    # 注意：用參數方式寫入 comments_title & VIDEO_ID
    subprocess.run([
        sys.executable,
        os.path.join(src_dir, "comment_catch.py"),
        video_id,
        comments_title
    ], check=True)
    st.success("留言已抓取完畢！")

    # 3. 執行 comment_clean.py
    st.write("清理留言資料中...")
    subprocess.run([
        sys.executable,
        os.path.join(src_dir, "comment_clean.py"),
        comments_title
    ], check=True)
    st.success("留言已清理完畢！")

    # 4. 執行 analyze.py 並取得情感統計
    st.write("分析留言情感中...")
    result = subprocess.run([
        sys.executable,
        os.path.join(src_dir, "analyze.py"),
        comments_title
    ], capture_output=True, text=True, check=True)
    # 解析 analyze.py 回傳的結果（需在 analyze.py print 最後統計結果為 dict 格式）
    import ast
    try:
        sentiment_counts = ast.literal_eval(result.stdout.strip().splitlines()[-1])
        st.write(f"情感統計結果：{sentiment_counts}")
    except Exception as e:
        st.error("情感分析回傳格式解析失敗")
        st.text(result.stdout)
        st.stop()

    # 5. 執行 pie_chart_generator.py
    st.write("產生圓餅圖中...")
    subprocess.run([
        sys.executable,
        os.path.join(src_dir, "pie_chart_generator.py"),
        comments_title,
        str(sentiment_counts.get('POSITIVE', 0)),
        str(sentiment_counts.get('NEGATIVE', 0))
    ], check=True)
    st.success("圓餅圖產生完畢！")

    # 6. 顯示圖片
    img_path = os.path.join(outputs_dir, f"{comments_title}.png")
    if os.path.exists(img_path):
        st.image(img_path, caption=f"{comments_title} 留言情緒分析", use_column_width=True)
    else:
        st.error(f"找不到圖片檔案：{img_path}")

