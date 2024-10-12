from flask import Flask
import os 
import markdown

app = Flask(__name__)
folder='articles/'

@app.route('/')
def listArticles():
    articles = []
    html = ''
    
    with open('template.html') as f:
        html = f.read()
    for f in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, f)):
            articles.append(f"- [{f}](/y/{f})") 
    
    content=markdown.markdown("\n".join(articles))

    return  html.replace('<flask-content/>',content)
@app.route('/y/<string:article>')
def browser(article):    
    try:
        html=''
        content=''
        with open('template.html') as f:
            html = f.read()
        with open(os.path.join(folder,article)) as f:
            content = markdown.markdown(f.read())
        return html.replace('<flask-content/>',content)
    except FileNotFoundError:
        return '',404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')