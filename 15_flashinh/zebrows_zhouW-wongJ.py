# ZhouLu - Wei Wen Zhou, Johnny Wong
# SoftDev1 pd8
# K15 -- Oh yes, perhaps I do…   
# 2018-10-2

from flask import Flask, render_template, request, session, url_for, redirect
import os

app = Flask(__name__)

# Encode cookies
app.secret_key = os.urandom(32);

@app.route("/")
def index():
    if "ZhouLu" in session:
        return render_template('welcome.html', user_welcome="ZhouLu")
    else:
        return render_template('form.html', title='welcome')

@app.route("/auth", methods=["POST"])
def authenticate():
    usr = request.form["name"]
    pw = request.form["pass"]

    if usr != "ZhouLu":
        return render_template("error.html",error_message="Incorrect username!")
    if pw != "abc1234":
        return render_template("error.html",error_message="Incorrect password!")
    
    # add username to session
    session[usr] = pw
    
    return redirect(url_for("index")) 
    
@app.route("/logout", methods=["POST"])
def logout():
    session.pop('ZhouLu')
    return redirect(url_for("index"))
    
if __name__ == "__main__":
    app.debug = True
    app.run()
