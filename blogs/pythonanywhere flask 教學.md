---
title: pythonanywhere flask 教學

---

# pythonanywhere flask 教學
免費主機
## flask
我經常使用flask模組來結合html完成我的網頁，但網頁需要上架，身為學生的我又沒什麼金錢，這時候，pythonanywhere就是一個好選擇，他支援flask，也自帶網域，缺點就是不能用cname，並且後面還有自己的consoles。
## pythonanywhere
[pythonanywhere](https://www.pythonanywhere.com/)，進去網站後右上方即可註冊，接著openweb:
![web](https://i.meee.com.tw/eAaMVU5.png)
接著因為我們沒有付費所以不能自訂domain name，下一步後選擇flask(當然別的也可)，接著進去後他應該就會跳到管理頁面，點擊files來編輯檔案，'flask_app.py'，假設我們程式是:
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'theoyu314159'
```
注意，不用放'run(debug = True)'之類的，接著就可以去我們製作好的網頁看看囉!