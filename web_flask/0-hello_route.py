#!/usr/bin/python3
"""
This script starts a Flask web application that listens on 0.0.0.0, port 5000.
The root route ("/") displays "Hello HBNB!".
"""
from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
