from flask import Flask, render_template
app = Flask(__name__)

@app.get("/")
def index():
    return "Hello, Flask"

@app.get("/home")
def home():
    return render_template("home.html", title="Flask 템플릿 연결")   

@app.get("/hw1")
def hw1():
    return render_template("rhkwp.html", title="러닝코스 추천 웹 기획서") 

if __name__=="__main__":
    app.run()