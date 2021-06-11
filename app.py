from flask import Flask, blueprints, jsonify
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

CORS(sources, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(sources, url_prefix='/api/v1/sources')

@app.route('/')
def hello():
	return 'Hello World!'

if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
