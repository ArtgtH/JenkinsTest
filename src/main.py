import flask


app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.jsonify({"result": "Hello World"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
