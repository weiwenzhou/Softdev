from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('form.html', title='welcome')

if __name__ == "__main__":
    app.debug = True
    app.run()
