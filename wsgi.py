import flask
application = flask.Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/cindy")
def cindy()
    return "Hello Cynthia!"

@application.route("/healthz")
def healthz():
    resp = flask.Response("ok")
    resp.headers['Custom-Header'] = 'okbyjim'
    return resp

if __name__ == "__main__":
    application.run()
