from flask import Flask, render_template
from datetime import date
import requests
app = Flask(__name__)



@app.route('/')
def home():
    api_endpoint = "https://api.npoint.io/e75e0e49fccb076f6e84"
    blogs = requests.get(api_endpoint)
    blog_data = blogs.json()
    return render_template("index.html", blogs=blog_data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
