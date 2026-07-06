from flask import Flask, request
import git

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask app is running!"


@app.route("/update_server", methods=["POST"])
def webhook():
    if request.method == "POST":
        repo = git.Repo("/home/myflaskapp1/my_flask_app")
        origin = repo.remotes.origin
        origin.pull()
        return "Updated PythonAnywhere successfully", 200
    else:
        return "Wrong event type", 400


if __name__ == "__main__":
    app.run()
