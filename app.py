from flask import Flask
import os
app = Flask(__name__)

if os.path.exists('counter.txt'):
    with open('counter.txt', 'r') as file:
        counter = int(file.read())
else:
    counter = 0

@app.route('/')
def hello_world():
    global counter
    counter += 1
    with open('counter.txt', 'w') as file:
        file.write(str(counter))
    return f"Hello! This page has been visited {counter} times."