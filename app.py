from flask import Flask, render_template

app = Flask(__name__)

lessons = [
    {
        "name": "Kaiser Wilhelm II",
        "url": "/kaiser"
    },
    {
        "name": "German society and economy in 1890",
        "url": "/society"
    },
    {
        "name": "Domestic reforms, Weltpolitik and the Naval Laws",
        "url": "/weltpolitik"
    },
    {
        "name": "The impact of the First World War",
        "url": "/ww1"
    },
    {
        "name": "The Weimar Constitution",
        "url": "/weimar"
    },
    {
        "name": "Political opposition and the Treaty of VersaillesThe impact of the First World War",
        "url": "/opposition"
    },
    {
        "name": "1923: Invasion of the Ruhr and hyperinflation",
        "url": "/ruhr"
    },
    {
        "name": "The early Nazi Party and the Munich Putsch",
        "url": "/munich"
    },
    {
        "name": "Stresemann and the 'Golden Years' (1924-29)",
        "url": "/munich"
    },
    {
        "name": "Reorganising the Nazi Party: the 'Lean Years' (1924-28)",
        "url": "/lean-years"
    },
    {
        "name": "The Great Depression and Nazi propaganda (1929-32)",
        "url": "/depression"
    },
]


@app.route('/')
def home():
    return render_template('index.html', lessons=lessons)

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
