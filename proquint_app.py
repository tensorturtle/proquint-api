'''
Minimal flask API application that returns a random proquint (pronounceable unique hash)

Usage: (from server point of view)
    pip install flask
    export FLASK_APP=proquint_app.py
    flask run
    curl localhost:5000

    (from user point of view)
    curl unique.tensorturtle.com

'''
import os
import proquint
from flask import Flask
app = Flask(__name__)

def generate_proquint():
    return proquint.uint2quint(int.from_bytes(os.urandom(4), byteorder="big", signed=False))

@app.route('/')
def index():
    return generate_proquint()
