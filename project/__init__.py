
""" Module summary:
Initialize the Flask application.
"""

from flask import Flask

from .views.index import index
from .views.login import login


############################################################################


# Initialize flask application:
app = Flask(__name__)

APPLICATION_NAME = "Teambuilder"

app.register_blueprint(index)
app.register_blueprint(login)
