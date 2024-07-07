
#import flask, request and function jsonify to create json response
from flask import Flask, request, jsonify 

#flask app
app = Flask(__name__)

#decorator - to make this accessible (slash is the path we want to access, the default route)
@app.route("/")

#function for route - contains data that we want user to have access to when they reach this route
def home():
    return "Home"

#to run our flask server
if __name__== "__main__":
    app.run(debug=True)