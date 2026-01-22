from flask import Flask, render_template, render_template_string
import os
import markdown
app = Flask(__name__)

BLOG_FOLDER = 'blogs'

@app.route('/')
def index():
    # return render_template('index.html')
    '''with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    # new_content = html_content.replace('<int/>', ' ')
    return render_template_string(html_content)'''

    path = os.path.join(BLOG_FOLDER, 'theo.md')
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 讀取 page.html 並顯示內容
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = markdown.markdown(content)
            return render_template_string(f.read().replace('<int/>', html_content))
    else:
        return "找不到該檔案", 404

@app.route('/about')
def about():
    with open('about.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    welcome = '<h2>歡迎來到我的程式小站</h2>\n <br> <p>這裡有很多有趣的程式文章，歡迎參觀！</p> <br> <p>作者：yulin</p> <br> <p>本網站使用的<a href="https://www.threads.com/@fusionwallvibe/post/DEpvKt8sk6o?hl=zh-hk" </a>模板<a href="https://www.threads.com/@fusionwallvibe/post/DEpvKt8sk6o?hl=zh-hk"></p> <br> <p>網站圖片來源<a href="https://www.threads.com/@wallpaperz_4you/post/DJT3cKmyjOM/hinata-wallpaper-cr-flux_ani-narutoshippuden-hinata-anime?hl=zh-hk"></a></p> <br> <p>版權所有 &copy; 2026 yulin</p>'
    new_content = html_content.replace('<about/>', welcome)
    return render_template_string(new_content)

@app.route('/msg')
def msg():
    with open('msg.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    # welcome = '<h2>歡迎來到我的程式小站</h2>\n <br> <p>這裡有很多有趣的程式文章，歡迎參觀！</p> <br> <p>作者：yulin</p> <br> <p>本網站使用的<a href="https://www.threads.com/@fusionwallvibe/post/DEpvKt8sk6o?hl=zh-hk" </a>模板<a href="https://www.threads.com/@fusionwallvibe/post/DEpvKt8sk6o?hl=zh-hk"></p> <br> <p>網站圖片來源<a href="https://www.threads.com/@wallpaperz_4you/post/DJT3cKmyjOM/hinata-wallpaper-cr-flux_ani-narutoshippuden-hinata-anime?hl=zh-hk"></a></p> <br> <p>版權所有 &copy; 2026 yulin</p>'
    #new_content = html_content.replace('<in/>', welcome)
    return render_template_string(html_content)

@app.route('/blogs')
def blogs():
    # 1. 取得所有檔名
    files = os.listdir(BLOG_FOLDER)
    
    # 2. 製作成一行一行的連結，點擊跳轉到 /page/檔名
    links = ""
    for name in files:
        links += f'<a href="/page/{name}">{name}</a><br>\n'
    
    # 3. 讀取 blogs.html 並替換標籤
    with open('blogs.html', 'r', encoding='utf-8') as f:
        return render_template_string(f.read().replace('<blogs/>', links))

@app.route('/page/<filename>')
def page(filename):
    path = os.path.join(BLOG_FOLDER, filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 讀取 page.html 並顯示內容
        with open('page.html', 'r', encoding='utf-8') as f:
            html_content = markdown.markdown(content)
            return render_template_string(f.read().replace('<word/>', html_content))
    else:
        return "找不到該檔案", 404

    '''with open('page.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    new_content = html_content.replace('<page/>', 'bbb')
    return render_template_string(new_content)'''

app.run(debug=True, host="0.0.0.0", port='5100')