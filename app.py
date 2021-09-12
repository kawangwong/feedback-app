from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates-ui")

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.debug = True ##In dev Flask setting, will referesh
    app.run