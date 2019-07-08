from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.jinja2')


if __name__ == '__main__':
    app.run()
