from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
    # return "<p>Hello, World!</p>"

@app.route('/this')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'welcome'

if __name__ =="__main__":
    app.run(debug=True)