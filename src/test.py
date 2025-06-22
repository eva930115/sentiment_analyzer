import os

# 取得目前腳本所在的資料夾路徑
script_dir = os.path.dirname(os.path.abspath(__file__))

# 取得專案根目錄（src 的上一層資料夾）
project_root = os.path.dirname(script_dir)

# 組出 data/input 路徑
folder_path = os.path.join(project_root, "data", "input")
file_path = os.path.join(folder_path, "test.csv")

# 確保資料夾存在
os.makedirs(folder_path, exist_ok=True)

# 建立 test.csv 檔案並寫入測試資料
with open(file_path, "w", encoding="utf-8") as f:
    f.write("id,name,score\n")
    f.write("1,Alice,90\n")
    f.write("2,Bob,85\n")

print(f"已經在 {file_path} 建立 test.csv！")
print("目前執行目錄：", os.getcwd())
print("實際建立檔案的完整路徑：", os.path.abspath(file_path))
