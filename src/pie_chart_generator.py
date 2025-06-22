import matplotlib.pyplot as plt
from matplotlib import rcParams
import os
import sys
import traceback

try:
        # CLI 參數處理
        if len(sys.argv) >= 4:
        comments_title = sys.argv[1]
        positive_comments = int(sys.argv[2])
        negative_comments = int(sys.argv[3])
        else:
        comments_title = 'test'
        positive_comments = 814
        negative_comments = 175

        rcParams['font.family'] = 'Microsoft JhengHei'
        rcParams['axes.unicode_minus'] = False

        labels = ['正面評論', '負面評論']
        sizes = [positive_comments, negative_comments]
        colors = ['#66b3ff', '#ff9999']
        explode = (0.05, 0)

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140,
                colors=colors, explode=explode, shadow=True)
        plt.title(f"情緒分布（總數 {positive_comments+negative_comments}）")
        plt.axis('equal')
        plt.tight_layout()

        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        output_folder = os.path.join(project_root, "outputs")
        os.makedirs(output_folder, exist_ok=True)
        output_path = os.path.join(output_folder, f"{comments_title}.png")
        plt.savefig(output_path)
        plt.close()

        print(f"圖檔已存到：{output_path}")

except Exception as e:
    print("錯誤發生：", e)
    traceback.print_exc()