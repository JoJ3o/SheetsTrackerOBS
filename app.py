from flask import Flask

app = Flask(__name__)


@app.route("/")
def update():
    return "<p>oi, mate</p>"
