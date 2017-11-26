
""" Module summary:
Functions:
  showIndex - Show site home.
"""

from flask import Blueprint, render_template
from project.database.dbconnect import mongo

############################################################################

index = Blueprint("index", __name__)

@index.route("/")
def showIndex():
  user_table = mongo.db.user
  
  # return "<h1>" + user_table.find({"name": "Joe"})[0]["name"] + "</h1>"
  
  return render_template("index.html")
