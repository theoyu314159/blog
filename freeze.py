from flask_frozen import Freezer
from app import app # 確保這裡匯入的是 app 物件

# 建議加入這項設定，讓輸出的連結更符合靜態網站需求
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'build2' # 打包後的資料夾名稱

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()