from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def blog():
    URL = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(URL)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
