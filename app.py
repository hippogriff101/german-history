from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/kaiser')
def lesson_one():
    return render_template('kaiser.html')

@app.route('/politics-of-90s')
def lesson_two():
    return render_template('political-system-1890s.html')

@app.route('/naval')
def lesson_three():
    return render_template('naval-lawes.html')

if __name__ == '__main__':
    app.run(debug=True)