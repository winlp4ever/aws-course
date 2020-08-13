from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/wait-a-minute")
def wait():
    return "<html><body>Wait wait wait!</body></html>"

@app.route("/about-me")
def foo():
    return "<h1>I'm a developer</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')