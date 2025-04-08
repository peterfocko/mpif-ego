from flask import Flask
from flask import request
import subprocess


app = Flask(__name__)


def gay():
    return """<html>
    <head>
        <title>GAY</title>
    </head>
    <body>
        <center><h1><u>GAY</u></h1></center>
    </body>
</html>
"""


def straight():
    return subprocess.check_output(["/usr/games/cowsay", "STRAIGHT"])


@app.route("/")
def ego():
    return straight() if "curl" in request.headers.get("user-agent", "").lower() else gay()


if __name__ == "__main__":
    app.run()
