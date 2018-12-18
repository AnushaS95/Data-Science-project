

from flask import Flask
import sqlite3
from flask import request
import json
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def retrieve():
   user = request.args.get('user')
   connection = sqlite3.connect('similarity.db')
   iterator = connection.cursor()
   statement = "SELECT * from users where id = " + user
   iterator.execute(statement)
   results = iterator.fetchall()
   data = {"user": user, "similar_users": [{"user": results[0][1], "similarity":results[0][2]}, {"user":results[0][3], "similarity":results[0][4]}, {"user":results[0][5], "similarity":results[0][6]}, {"user":results[0][7], "similarity":results[0][8]}]}
   data = jsonify(data)
   print data.get_json()['user'], data.get_json()['similar_users'][3]['user'], data.get_json()['similar_users'][3]['similarity']
   return data

if __name__ == "__main__":
   app.run()
