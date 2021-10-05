from gevent import monkey; monkey.patch_all()
import sheets
import time
import json
from gevent.pywsgi import WSGIServer
from flask import Flask, jsonify, Request, render_template, Response, stream_with_context

# app.py
app = Flask(__name__)


@app.route('/hello')
def getData():
    message = json.dumps(sheets.main())
    return message  # serialize and use JSON headers


@app.route('/test')
def test_page():
    # look inside `templates` and serve `index.html`
    return render_template('index.html')


@app.route('/listen')
def listen():
    def respondToClient():
        while True:
            _data = json.dumps(sheets.main())
            yield f"id: 1\ndata: {_data}\nevent: online\n\n"
            time.sleep(5)

    return Response(respondToClient(), mimetype='text/event-stream')


@app.route('/test2')
def testPage():
    return render_template('index2.html')


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port="5000")
    httpServer = WSGIServer(("0.0.0.0", 5000), app)
    httpServer.serve_forever()
