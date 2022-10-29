from flask import Flask, render_template
app = Flask(__name__)
from waitress import serve

@app.route("/")
def index():
    homepage = "<h1>顏愷升的求職相關資訊</h1>"
    homepage +="<h2>班級：資管2B<h2>"
    homepage +="<h2>學號：411025198<h2>"
    homepage += "<a href=/aboutme>我的個人簡介</a><br>"
    homepage += "<a href=/hlm>興趣何倫碼測驗結果</a><br>"
    homepage += "<a href=/welcome>MIS相關工作介紹</a><br>"
    homepage += "<a href=/www>我的自傳履歷</a><br>"


    return homepage

@app.route("/aboutme")
def aboutme():
    return render_template("aboutme.html")

@app.route("/hlm")
def today():
    return render_template("hlm.html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


@app.route("/www")
def zizhuan():
    return render_template("www.html")
 


if __name__ == "__main__":
    #app.run()
    serve(app, host='0.0.0.0', port=8080)


