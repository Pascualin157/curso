
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prac_js')
def prac_JS():
    return render_template('html/prac_js.html')

@app.route('/prac_PY')
def prac_PY():
    return render_template('html/prac_PY.html')

@app.route('/prac_numpy')
def prac_numpy():
    return render_template('html/prac_numpy.html')

@app.route('/prac_pandas')
def prac_pandas():
    return render_template('html/prac_pandas.html')


    
if __name__ == '__main__':
    app.run(debug=True , port=5100)