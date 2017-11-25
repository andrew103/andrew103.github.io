
""" Module summary:
Functions:
  showIndex - Show site home.
"""

from flask import Blueprint, render_template

############################################################################

index = Blueprint("index", __name__)

@index.route("/")
def showIndex():

  return render_template("index.html")
