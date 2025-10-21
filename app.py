from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
 return "<p>hello, world  just checking!</p>"

if __name__ == "__main__":
    app.run(debug=True)

git init