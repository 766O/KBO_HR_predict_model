
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_pybo():
    return '강재원 병씬'