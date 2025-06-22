
import matplotlib.pyplot as plt
from matplotlib import rcParams
import os

comments_title  = 'test'  # 使用者自訂檔案名稱（不含 .csv）
positive_comments = 814
negative_comments = 175

# 設定中文字型（Windows 建議用 Microsoft JhengHei）
rcParams['font.family'] = 'Microsoft JhengHei'
rcParams['axes.unicode_minus'] = False  # 解決負號無法顯示的問題

# 數據
labels = ['正面評論', '負面評論']
sizes = [positive_comments, negative_comments]
colors = ['#66b3ff', '#ff9999']
explode = (0.05, 0)  # 突出顯示正面評論

# 畫圖
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140,
        colors=colors, explode=explode, shadow=True)
plt.title(f"情緒分布（總數 {positive_comments+negative_comments}）")
plt.axis('equal')
plt.tight_layout()


# ====== 路徑組合區 ======
# 取得目前腳本所在目錄
script_dir = os.path.dirname(os.path.abspath(__file__))
# 專案根目錄（src的上一層）
project_root = os.path.dirname(script_dir)
# output 資料夾路徑
output_folder = os.path.join(project_root, "outputs")
os.makedirs(output_folder, exist_ok=True)
# 圖檔完整路徑
output_path = os.path.join(output_folder, f"{comments_title}.png")
# ====== 儲存圖表 ======
plt.savefig(output_path)
plt.close()

print(f"圖檔已存到：{output_path}")