from flask import Flask, render_template, request
from flask_alchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates-ui")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods = ['POST'])
def submit():
    if request.method == "POST":
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        if customer == '' or dealer == '':
            return render_template("index.html", message = "You did not input the necessary fields")
        return render_template("success.html")

if __name__ == '__main__':
    app.debug = True ##In dev Flask setting, will referesh
    app.run