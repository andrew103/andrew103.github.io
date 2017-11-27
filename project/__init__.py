
""" Module summary:
Initialize the Flask application.
"""

from flask import Flask
from flask_pymongo import PyMongo
from .database.dbconnect import mongo

from .views.index import index
from .views.login import login

from .apis import apis

############################################################################


# Initialize flask application:
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'teambuilderdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/teambuilderdb'

mongo.init_app(app)

APPLICATION_NAME = "Teambuilder"

app.register_blueprint(index)
app.register_blueprint(login)
app.register_blueprint(apis)
