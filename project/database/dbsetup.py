
# To-do: create chat table!

from flask_pymongo import PyMongo, MongoClient
import datetime

# MongoClient represents the connection to the MongoDB instance that 
# runs on port 27017 on the localhost.
client = MongoClient('mongodb://localhost:27017/')

# Can access database with either of the methods shown below.
# MongoDB creates new databases implicitly upon their first use. Same for 
# collections?

# mydb = client.teambuilderdb
mydb = client['teambuilderdb']


#####################################

# Collection in a MongoDB is like a table in an RDBMS.
# Drop and regenerate collections (tables) when this file is run:
mydb.user.drop()
mydb.project.drop()


user_records = [
  { "name": "Joe",
    "summary": "Developer ...",
    "email": "Joe@email.com",
    "skills": ["JavaScript", "React", "Java"],
    "roles": ["Front end"],
    "project_favorites": None,
    "date" : datetime.datetime.utcnow()
  },

  { "name": "Jack",
    "summary": "Front-end Engineer ...",
    "email": "Jack@email.com",
    "skills": ["CSS", "AngularJS"],
    "roles": ["Back end"],
    "project_favorites": None,
    "date" : datetime.datetime.utcnow()
  }
]

user_ids = mydb.user.insert(user_records)


project_records = [
  { "name": "Project_1",
    "summary": "Project summary ...",
    "skills": ["JavaScript", "React", "Java"],
    "roles": ["Front end", "Full stack"],
    "team_members": user_ids,
    "is_active": True,
    "date" : datetime.datetime.utcnow()
  }
]

project_ids = mydb.project.insert(project_records)


## Add a favorited project to the first user profile:
mydb.user.update({"_id": user_ids[0]}, 
                 {"$set": {"project_favorites": project_ids[0]}})


# for s in mydb.user.find():
 # print s['_id']

# for s in mydb.project.find():
 # print s["team_members"]
