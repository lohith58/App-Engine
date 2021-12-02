from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hey hi lohith this is first MicroService - V1'