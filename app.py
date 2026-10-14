from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Lesson 1
@app.route('/kaiser')
def kaiser():
    return render_template('kaiser.html')

@app.route('/society')
def society():
    return render_template('society.html')

# Lesson 2
@app.route('/weltpolitik')
def weltpolitik():
    return render_template('weltpolitik.html')

# Lesson 3
@app.route('/ww1')
def ww1():
    return render_template('ww1.html')

@app.route('/weimar')
def weimar():
    return render_template('weimar.html')

# Lesson 4
@app.route('/opposition')
def opposition():
    return render_template('opposition.html')

# Lesson 5
@app.route('/ruhr')
def ruhr():
    return render_template('ruhr.html')

# Lesson 6
@app.route('/munich')
def munich():
    return render_template('munich.html')

# Lesson 7
@app.route('/stresemann')
def stresemann():
    return render_template('stresemann.html')

# Lesson 8
@app.route('/lean-years')
def lean_years():
    return render_template('lean-years.html')

# Lesson 11
@app.route('/depression')
def depression():
    return render_template('depression.html')

if __name__ == '__main__':
    app.run(debug=True)
