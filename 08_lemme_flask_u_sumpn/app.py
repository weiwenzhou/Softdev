#Wei Wen Zhou
#SoftDev pd8
#K#08 -- Fill Yer Flask
#2018-09-19

from flask import Flask

app = Flask(__name__) # create instance of class Flask

@app.route("/") # assign fxn to route
def home():
    return '''
        Hello! Welcome to WW\'s page. <br> 
        <a href=/assignments> Click here for assignments page</a> <br>
        <a href=/lct> Click here for LCT page</a> <br>
        
    '''
@app.route("/assignments")
def assignments():
    return '<a href="https://docs.google.com/document/u/1/d/e/2PACX-1vQDkHCRKND99iCgSfbr7Y8-SvwwO_xQVHTjK2kmJqNawfZQUITFS2quraRPJp3XHtipAYFfvhBRwVZi/pub"> Assignments for Softdev </a>'
    
@app.route("/lct")
def lct():
    return '''
        <a href="https://github.com/stuy-softdev/notes-and-code/tree/master/6"> LCT for Period 6 </a> <br>
        <a href="https://github.com/stuy-softdev/notes-and-code/tree/master/7"> LCT for Period 7 </a> <br>
        <a href="https://github.com/stuy-softdev/notes-and-code/tree/master/8"> LCT for Period 8 </a> <br>
    
    '''
if __name__ == "__main__":
    app.debug = True
    app.run()
