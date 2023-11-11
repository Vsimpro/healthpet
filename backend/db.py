import os, dotenv, pymysql
dotenv.load_dotenv()

### HELPING METHODS ###
def test(connection):
    try:
        # Create cursor
        cursor = connection.cursor()

        # Dump test data
        cursor = create_table(cursor, "mytest", "(id INTEGER PRIMARY KEY)")
        cursor = insert_into(cursor, table="mytest", columns="(id)", values="(1), (2)")
        cursor = query(cursor, "SELECT * FROM mytest")

        # print result
        print(cursor.fetchall())
        
    finally:
        # close connection
        connection.close()

def create_connection():
    timeout = 10
    connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db=os.getenv("DB_NAME"),
        host=os.getenv("DB_HOST"),
        password=os.getenv("DB_PASSWORD"),
        read_timeout=timeout,
        port=26718,
        user=os.getenv("DB_USER"),
        write_timeout=timeout,
    )

    return connection

### DATABASE METHODS ###

# Example:
# create_table(cursor, "mytest", "(id INTEGER PRIMARY KEY)")  
def create_table(_cursor, table=None, columns=None):
    t,co,cu = table == None, columns == None, _cursor == None
    if t or cu or co:
       print("[!] Value for", "table"*t, "columns"*co, "cursor"*cu ,"can not be", None)
       return _cursor

    _cursor.execute(f"CREATE TABLE IF NOT EXISTS {table} {columns}")
    return _cursor


# Example:
# insert_into(cursor, table="mytest" columns="(id)" values="(1), (2)")
def insert_into(_cursor, table, values, columns):
    #TODO: Do Validation to prevent SQLi
    t,co,cu,va = table == None, columns==None, _cursor == None,  values == None
    if t or cu or co or va:
       print("[!] Value for", "table"*t, "columns"*co, "cursor"*cu, "values"*va, "can not be 'None'")
       return _cursor

    _cursor.execute(f"INSERT INTO {table} {columns} VALUES {values}")
    return _cursor


def query(_cursor, query):
    cu, qu = _cursor == None, query == None
    if cu or qu:
       print("[!] Value for", "cursor"*cu, "query"*qu, "can not be 'None'")
       return _cursor
    
    _cursor.execute(query)
    return _cursor
