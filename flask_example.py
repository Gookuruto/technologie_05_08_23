import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p><b>Hello</b>, World!</p>"


@app.route("/chuck")
def chuck_joke():
    joke = requests.get("https://api.chucknorris.io/jokes/random")
    return f"<div>><p>{joke.json()['value']}</p><p><a href='http://127.0.0.1:5000/chuck'>next joke</a></p></div>"


app.run()
