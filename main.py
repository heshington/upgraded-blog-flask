from flask import Flask, render_template
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

@app.route('/post/<int:id>')
def get_blog(id):
    api_endpoint = "https://api.npoint.io/e75e0e49fccb076f6e84"
    blogs = requests.get(api_endpoint)
    blog_data = blogs.json()
    for blog in blog_data:
        if blog['id'] == id:
            title = blog['title']
            subtitle = blog['subtitle']
            author = blog['author']
            image = blog['image']
            date = blog['date']
            body = blog['body']
    return render_template('post.html', title=title,subtitle=subtitle, author=author, image=image, date=date, blog=body)

if __name__ == "__main__":
    app.run(debug=True)
