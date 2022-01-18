from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods = ['POST'])
def process():
    session['name'] = request.form['name']
    session['city'] = request.form['city']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("results.html")

@app.route('/return')
def go_back():
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)