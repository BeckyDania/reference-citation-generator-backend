from flask import Flask, blueprints, jsonify, after_this_request
from resources.sources import sources  


import models

from flask_cors import CORS

import os
from dotenv import load_dotenv

load_dotenv()

DEBUG=True 
PORT=8000

app = Flask(__name__)

app.secret_key = (os.environ.get("FLASK_APP_SECRET"))
print(os.environ.get("FLASK_APP_SECRET"))

CORS(sources, origins=['http://localhost:3000', 'https://limitless-harbor-frontend.herokuapp.com'], supports_credentials=True)

app.register_blueprint(sources, url_prefix='/api/v1/sources')

@app.before_request 

def before_request():

    """Connect to the db before each request"""
    print("you should see this before each request") # optional -- to illustrate that this code runs before each request -- similar to custom middleware in express.  you could also set it up for specific blueprints only.
    models.DATABASE.connect()

    @after_this_request # use this decorator to Executes a function after this request
    def after_request(response):
        """Close the db connetion after each request"""
        print("you should see this after each request") # optional -- to illustrate that this code runs after each request
        models.DATABASE.close()
        return response # go ahead and send response back to client
                      # (in our case this will be some JSON)

@app.route('/')
def hello():
	return 'Hello World!'

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)

if os.environ.get('FLASK_ENV') != 'development':
  print('\non heroku!')
  models.initialize()