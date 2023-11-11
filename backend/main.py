from flask import Flask, jsonify
from flask_cors import CORS

from db import *


### Global Variables ###
db_conn = None
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

### Methods
def query_helper(_query):
    _db_data = ""
    try: 
        _cursor  = query(create_connection().cursor(), _query) 
        
        _db_data = _cursor.fetchall()
    except Exception as e:
        print("[!] Error in helper", e)

    return _db_data

def prepare_db():
    try:
        # Create Connection
        _connection = create_connection()

        # Create cursor
        cursor = _connection.cursor()

        # Create tables
        
        """ Uncomment when creating a new DB
        cursor = create_table(cursor, table="user",   columns="(id INTEGER PRIMARY KEY, name VARCHAR(255))")
        cursor = create_table(cursor, table="steps",  columns="(id INTEGER PRIMARY KEY, user_id INTEGER, steps INTEGER, date DATE)")
        cursor = create_table(cursor, table="stress", columns="(id INTEGER PRIMARY KEY, user_id INTEGER, level INTEGER, level_min INTEGER, level_max INTEGER, date DATE )")
        cursor = create_table(cursor, table="sleep",  columns="(id INTEGER PRIMARY KEY, user_id INTEGER, time INTEGER, date DATE)")
        """

        # Insert Example data
        """ Uncomment when creating a new DB
        # Matti M:
        cursor = insert_into(cursor, table="user",    columns="(id, name)",                                       values="(0, 'Matti M.')")
        cursor = insert_into(cursor, table="steps",   columns="(id, user_id, steps, date)",                       values="(1, 0, 11239, '2023-10-11')")
        cursor = insert_into(cursor, table="stress",  columns="(id, user_id, level, level_min, level_max, date)", values="(1, 0, 54, 23, 73, '2023-10-11')")
        cursor = insert_into(cursor, table="sleep",   columns="(id, user_id, time, date)",                        values="(1, 0, 510, '2023-10-10')")
        

        # Anni A:
        cursor = insert_into(cursor, table="user",    columns="(id, name)",                                       values="(1, 'Anni A.')")
        cursor = insert_into(cursor, table="steps",   columns="(id, user_id, steps, date)",                       values="(2, 1, 6012, '2023-10-11')")
        cursor = insert_into(cursor, table="stress",  columns="(id, user_id, level, level_min, level_max, date)", values="(2, 1, 10, 51, 65, '2023-10-11')")
        cursor = insert_into(cursor, table="sleep",   columns="(id, user_id, time, date)",                        values="(2, 1, 300, '2023-10-10')")
        cursor = insert_into(cursor, table="sleep",   columns="(id, user_id, time, date)",                        values="(3, 2, 470, '2023-10-10')")


        # Pekka P:
        cursor = insert_into(cursor, table="user",    columns="(id, name)",                                       values="(2, 'Pekka P.')")
        cursor = insert_into(cursor, table="steps",   columns="(id, user_id, steps, date)",                       values="(3, 2, 500, '2023-10-11')")
        cursor = insert_into(cursor, table="stress",  columns="(id, user_id, level, level_min, level_max, date)", values="(3, 2, 62, 15, 99, '2023-10-11')")


        # Sari S:
        cursor = insert_into(cursor, table="user",    columns="(id, name)",                                       values="(3, 'Sari S.')")
        cursor = insert_into(cursor, table="steps",   columns="(id, user_id, steps, date)",                       values="(4, 3, 13129, '2023-10-11')")
        cursor = insert_into(cursor, table="stress",  columns="(id, user_id, level, level_min, level_max, date)", values="(4, 3, 23, 8, 67, '2023-10-11')")
        cursor = insert_into(cursor, table="sleep",   columns="(id, user_id, time, date)",                        values="(4, 3, 600, '2023-10-10')")
        """

        
        # Query example data
        cursor = query(cursor, "SELECT * FROM user, steps, stress, sleep")

        # print result
        print(cursor.fetchall())

        # Commit changes.
        _connection.commit()
        
    finally:
        # Close connection
        _connection.close()


### API Routes
# index, check connection is ok.
@app.route("/")
def index():
    return "200"

# fetch all data
@app.route("/data")
def data():
    response = None
    try:
        response = query_helper( "SELECT * FROM user, steps, stress, sleep" )
    except Exception as e:
        print("[!] Error in /user. ", e)

    return jsonify( dict(response) )

# Get user data
@app.route("/user")
def user():
    response = None
    
    try:
        response = query_helper( "SELECT * FROM user" )
    except Exception as e:
        print("[!] Error in /user. ", e)

    return jsonify( dict(response) )

# Get sleep data
@app.route("/sleep/<user_id>")
def sleep(user_id):
    response = None
    try:
        response = query_helper( f"SELECT * FROM sleep WHERE user_id = {int( user_id )}" )
    except Exception as e:
        print("[!] Error in /sleep. ", e)

    return jsonify( dict(response[0]) )

# Get step data
@app.route("/steps/<user_id>")
def steps(user_id):
    response = None
    try:
        response = query_helper( f"SELECT * FROM steps WHERE user_id = {int( user_id )}" )
    except Exception as e:
        print("[!] Error in /steps. ", e)

    return jsonify( dict(response[0]) )

# Get step data
@app.route("/stress/<user_id>")
def stress(user_id):
    response = None
    try:
        response = query_helper( f"SELECT * FROM stress WHERE user_id = {int( user_id )}" )
    except Exception as e:
        print("[!] Error in /stress. ", e)

    return jsonify( dict(response[0]) )


### initialize db ###
def main():
    prepare_db()

if __name__ == "__main__":
    main()
    app.run(host="0.0.0.0", port=8081)
