from flask import Flask, render_template
import requests

post = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/index.html')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)