from flask import Flask
from welcome import greet

app = Flask(__name__)


@app.route('/', methods= ["GET"])
def welcome():
    return greet()

if __name__=='__main__':
   app.run(host="0.0.0.0",debug = True)










