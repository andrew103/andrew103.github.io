
from flask import Blueprint, jsonify, render_template, request
from project.database.dbconnect import mongo

############################################################################

apis = Blueprint("apis", __name__)

@apis.route("/api/projects")
def apiProjects():
  user_table = mongo.db.user
  
  filter_dict = {}
  for par_name in request.args.keys():
    tmp_list = request.args[par_name].split(",")
    filter_dict[par_name] = { "$in": tmp_list }
  print filter_dict
  
  
  if "skills" in request.args:
    # Instead of creating a list of skills, could do a regex ...
    skills_list = request.args["skills"].split(",")
    cursor = user_table.find(filter_dict)
    users = list(cursor)

    for i in range(len(users)):
      users[i]["id"] = str(users[i]["_id"])
      del users[i]["_id"]   # id object not serializable
      
    return jsonify(users = users)
    
  # For now, if there's an error, render the index page:
  return render_template("index.html")
