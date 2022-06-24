from flask import Flask, render_template
from flask import request
import feedparser
 
app = Flask(__name__)
 
 
@app.route('/')
def index():
    return render_template('index.html', title='RSS')
 
 
@app.route('/rss', methods=['POST'])
def rss():
    url = request.form['rss_url']
    # return request.form['rss_url']
    dictionary = feedparser.parse(url)
    # pythonオブジェクトからJSON文字列に変換して返す
    print("flaskから出力")
    print("RSSの情報の数")
    print(type(dictionary.entries))
    print(len(dictionary.entries))
 
    import json
 
    return json.dumps(dictionary.entries)
 
 
@ app.route('/rss_page')
def rss_page():
    #     url = request.form['rss_url']
    #     # return request.form['rss_url']
    #     dictionary = feedparser.parse(url)
    #     # pythonオブジェクトからJSON文字列に変換して返す
    #     import json
    #     url_dict = json.dumps(dictionary.entries)
 
    #     # return json.dumps(dictionary.entries)
    #     return render_template('rss_page.html', title='RSS', url_result="url_dict")
    return render_template('rss_page.html', title='RSS')
 
 
if __name__ == "__main__":
    app.run(port=8000, debug=True)