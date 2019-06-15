from flask import Flask
import random


app = Flask(__name__)

@app.route("/")
def hello():
    return "hey whats up hows it going "

@app.route("/shit")
def newone():
    return "wassup g"

@app.route("/<name>")
def helloName(name):
    return "hey whats up hows it going " + name


@app.route("/random")
def randomNumGen():
    return str(random.randint(0,100))