from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tym')
def tym():
    return render_template('tym.html')

@app.route('/hraci')
def hraci():
    return render_template('hraci.html')

@app.route('/udalosti')
def udalosti():
    return render_template('udalosti.html')

@app.route('/e-shop')
def eshop():
    return render_template('e-shop.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/produkty/dres.html')
def dres():
    return render_template('produkty/dres.html')

@app.route('/produkty/klobouk.html')
def klobouk():
    return render_template('produkty/klobouk.html')

if __name__ == '__main__':
    app.run(debug=True)
