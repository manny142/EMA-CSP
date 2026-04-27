#What does Flask do?
#What are the steps to setting up a Flask project?
#How can you reference subpages on your Flask project? (Meaning the difference between the home page and a personal profile)
#What are templates?
from flask import flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

    if __name__ == "__main__":
        app.run()