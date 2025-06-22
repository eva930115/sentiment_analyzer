from googleapiclient.discovery import build
import pandas as pd
import os

# ✅ API 金鑰與影片 ID
API_KEY = 'AIzaSyDfR0Jxd2Oi0xHq5BOmmz6rFPxTvZEspCg'
VIDEO_ID = 'YbJOTdZBX1g'  # 例如 'dQw4w9WgXcQ'

# ✅ 自訂輸出檔案名稱（不含副檔名 .csv）
comments_title = 'test'  # 可讓使用者輸入 YouTube_Rewind_2018、CES_2025_Keynote

# ✅ 建立 YouTube API 物件
youtube = build('youtube', 'v3', developerKey=API_KEY)
comments = []

# ✅ 最多留言數
MAX_COMMENTS = 1000

# ✅ 抓取留言函式
def get_comments(video_id):
    next_page_token = None
    count = 0

    while count < MAX_COMMENTS:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            pageToken=next_page_token,
            textFormat="plainText"
        )
        response = request.execute()

        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "author": comment["authorDisplayName"],
                "text": comment["textDisplay"],
                "published": comment["publishedAt"],
                "likeCount": comment["likeCount"]
            })
            count += 1
            if count >= MAX_COMMENTS:
                break

        if "nextPageToken" not in response or count >= MAX_COMMENTS:
            break

# ✅ 執行抓取
get_comments(VIDEO_ID)

# ✅ 儲存抓取的資料
# 取得目前腳本所在的資料夾路徑
script_dir = os.path.dirname(os.path.abspath(__file__))

# 取得專案根目錄（src 的上一層資料夾）
project_root = os.path.dirname(script_dir)

# 組出 data/input 路徑
folder_path = os.path.join(project_root, "data", "input")

# 檔案名稱
output_filename = f"{comments_title}.csv"
output_path = os.path.join(folder_path, output_filename)

# 確保資料夾存在
os.makedirs(folder_path, exist_ok=True)

# 儲存 DataFrame
df = pd.DataFrame(comments)
df.to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"✅ 已儲存 {len(df)} 筆留言到：{output_path}")