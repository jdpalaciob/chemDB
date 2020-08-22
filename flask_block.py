""" Script to develop the API REST block of chemDB """

from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def homepage(name):
    return f'Hello {name}'

if __name__ == "__main__":
    app.debug = False
    app.run()
