import sheets

# app.py
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)


@app.route('/hello')
def getData():
    message = str(sheets.main())
    return message  # serialize and use JSON headers


@app.route('/test')
def test_page():
    # look inside `templates` and serve `index.html`
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
