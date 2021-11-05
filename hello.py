from flask import Flask
from flask import make_response, render_template
from time import sleep as sleep
from random import randrange as randrange

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("homepage.html")
    # return "hello world"

@app.route("/health")
def health():
    return {"status": 200}

@app.route("/endpoint")
def endpoint():
    return {
        "message": "Stop hitting me!"
    }

@app.route("/badendpoint")
def badendpoint():
    resp = make_response("I don't work", 400)
    return resp

@app.route("/slowendpoint")
def slowendpoint():
    resp = make_response("I should work slowly", 200)
    sleep(randrange(3, 6))
    return resp