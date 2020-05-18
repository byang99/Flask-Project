###################
#
# Name: Brian Yang
# UNI: by2289
# ENGI 1006 Final
#
# Python Flask routes
#
###################


#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/1006")
def a1006():
    return render_template("1006.html")

@app.route("/assignments")
def assignments():
    return render_template("assignments.html")

@app.route("/classes")
def classes():
    return render_template("classes.html")


#start the server
if __name__ == "__main__":
    app.run()