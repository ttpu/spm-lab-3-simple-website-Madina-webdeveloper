from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/content_page')
def content_page():
    return render_template('content.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)