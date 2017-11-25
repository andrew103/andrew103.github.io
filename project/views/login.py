
""" Module summary:
Functions:
"""

from flask import Blueprint, render_template

############################################################################

login = Blueprint("login", __name__)

@login.route("/login")
def showLogin():
  return "<h3>Login stuff</h3>"

  
@login.route('/search-example')
def search():
    return render_template('search.html')
