from flask import Flask
import os 

app = Flask(__name__)
folder='articles/'

@app.route('/y/list')
def listArticles():
    articles=[]
    for f in os.listdir(folder):
        if os.path.isfile(os.path.join(folder, f)):
            articles.append(f) 
    return "<br>".join(articles)

@app.route('/y/<string:article>')
def browser(article):    
    try:
        with open(os.path.join(folder,article)) as f:
            return f.read()
    except FileNotFoundError:
        return '',404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')