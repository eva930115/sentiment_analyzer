from googleapiclient.discovery import build
import pandas as pd
import os
import sys

# CLI 參數處理
if len(sys.argv) >= 3:
    VIDEO_ID = sys.argv[1]
    comments_title = sys.argv[2]
else:
    VIDEO_ID = 'YbJOTdZBX1g'   # 預設範例
    comments_title = 'test'     # 預設範例

API_KEY = 'AIzaSyDfR0Jxd2Oi0xHq5BOmmz6rFPxTvZEspCg'

youtube = build('youtube', 'v3', developerKey=API_KEY)
comments = []
MAX_COMMENTS = 1000

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

get_comments(VIDEO_ID)

# 路徑組合
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
folder_path = os.path.join(project_root, "data", "input")
output_filename = f"{comments_title}.csv"
output_path = os.path.join(folder_path, output_filename)
os.makedirs(folder_path, exist_ok=True)

df = pd.DataFrame(comments)
df.to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"✅ 已儲存 {len(df)} 筆留言到：{output_path}")
