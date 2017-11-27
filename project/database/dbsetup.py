
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
    "date" : datetime.datetime.utcnow()
  },

  { "name": "Jack",
    "summary": "Front-end Engineer ...",
    "email": "Jack@email.com",
    "skills": ["CSS", "AngularJS"],
    "roles": ["Back end"],
    "date" : datetime.datetime.utcnow()
  }
]

user_ids = mydb.user.insert(user_records)


project_records = [
  { "name": "Joe",
    "summary": "Developer ...",
    "skillsNeeded": ["JavaScript", "Reach", "Java"],
    "rolesNeeded": ["Front end", "Full stack"],
    "team_members": user_ids,
    "date" : datetime.datetime.utcnow()
  }
]

mydb.project.insert(project_records)


# for s in mydb.user.find():
 # print s['_id']

# for s in mydb.project.find():
 # print s["team_members"]
