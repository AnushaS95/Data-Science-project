

from flask import Flask
import sqlite3
from flask import request

app = Flask(__name__)

@app.route("/")
def retrieve():
   user = request.args.get('user')
   connection = sqlite3.connect('similarity.db')
   iterator = connection.cursor()
   statement = "SELECT * from users where id = " + user
   iterator.execute(statement)
   results = iterator.fetchall()
   display = "4 Most similar users to User {0} are <br><br>User - {1} with similarity of {2}<br>User - {3} with similarity of {4}<br>User - {5} with similarity of {6}<br>User - {7} with similarity of {8}".format(user, results[0][1], results[0][2], results[0][3], results[0][4], results[0][5], results[0][6], results[0][7], results[0][8])
   return display

if __name__ == "__main__":
   app.run()
