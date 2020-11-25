import flask
app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/healthz")
def healthz():
    resp = flask.Response("ok")
    resp.headers['Custom-Header'] = 'okbyjim'
    return resp

if __name__ == "__main__":
    app.run()
