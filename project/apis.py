
from flask import Blueprint, jsonify, render_template, request
from project.database.dbconnect import mongo
import json
from bson import json_util

############################################################################

apis = Blueprint("apis", __name__)

@apis.route("/api/users")
def apiUsers():
  user_table = mongo.db.user
  
  filter_dict = {}
  for par_name in request.args.keys():
    # Instead of creating lists of skills, could do a regex ...
    tmp_list = request.args[par_name].split(",")
    filter_dict[par_name] = { "$in": tmp_list }

  cursor = user_table.find(filter_dict)
  users = list(cursor)
  
  if users:
    # This deals with the custom Pymongo data objects, esp. Object ID.
    users = json.dumps(users, default=json_util.default)
    return users
    
  # For now, if there's an error, render the index page:
  return render_template("index.html")


@apis.route("/api/projects")
def apiProjects():
  project_table = mongo.db.project
  
  filter_dict = {}
  for par_name in request.args.keys():
    # Instead of creating lists of skills, could do a regex ...
    tmp_list = request.args[par_name].split(",")
    filter_dict[par_name] = { "$in": tmp_list }

  cursor = project_table.find(filter_dict)
  projects = list(cursor)
  
  if projects:
    projects = json.dumps(projects, default=json_util.default)
    return projects
    
    ## This was my original attempt at jsonifying.
    ## Leaving it here while I'm still figuring this out.
    # for i in range(len(projects)):
      # projects[i]["id"] = str(projects[i]["_id"])
      # projects[i]["team_members"] = \
        # [str(x) for x in projects[i]["team_members"]]
      # del projects[i]["_id"]   # id object not serializable
    # return jsonify(projects = projects)
    
  # For now, if there's an error, render the index page:
  return render_template("index.html")
