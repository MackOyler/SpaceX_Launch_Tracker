from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world! updated"

if __name__ == "__main__":
    app.run(debug=True)