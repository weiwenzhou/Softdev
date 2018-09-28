from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('form.html', title="Submit Form")
    
@app.route("/auth")
def auth():
    return render_template('out.html', 
                            title="Submission Complete",
                            user=request.args['username'],
                            method=request.method)

if __name__ == "__main__":
    app.debug = True
    app.run()