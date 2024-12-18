from flask import Flask, jsonify, redirect, url_for

## 1xx informational
## 2xx success
## 3xx redirect
## 4xx client error
## 5xx server error

app = Flask(__name__)

@app.route('/Continue')
def _continue():
    return "hello", 100

@app.route('/')
def _switching():
    return "hello", 101

@app.route('/')
def _processing():
    return "hello", 102

@app.route('/')
def _early_hints():
    return "hello", 103

if __name__ == '__main__':
    app.run(debug=True)