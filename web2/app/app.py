from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
    return "WEB2 OK"

@app.get("/health")
def health():
    return "OK"
