
#import flask, request and function jsonify to create json response
from flask import Flask, request, jsonify 

#flask app
app = Flask(__name__)

#decorator - to make this accessible (slash is the path we want to access, the default route)


#to run our flask server
if __name__== "__main__":
    app.run(debug=True)