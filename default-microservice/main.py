from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hey hi lohith this default MicroService - V1'