import sqlite3
from flask import g

# this is the path to the database file that will be created in the root of the project
DATABASE_URL = "main.db"

# this function help us to connect to the database and return the connection object to the database
def get_db():
  db = getattr(g, '_database', None)
  if db is None:
    db = g._database = sqlite3.connect(DATABASE_URL)
  return db