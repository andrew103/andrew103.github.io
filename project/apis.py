
from flask import Blueprint, jsonify, render_template
from project.database.dbconnect import mongo

############################################################################

apis = Blueprint("apis", __name__)

@apis.route("/api/projects")
def apiProjects():
  user_table = mongo.db.user
  
  tmp = user_table.find({"name": "Joe"})[0]
  del tmp["_id"]    # id object not jsonifiable
  
  return jsonify(tmp)
  