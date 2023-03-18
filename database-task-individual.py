import sqlite3
from sqlite3 import Error

def create_connection(db_chosen):
    connection = None
    try:
        connection = sqlite3.connect(db_chosen)
    except Error as er:
        print(er)
    return connection

def execute_sql(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except Error as er:
        print(er)



if __name__ == "__main__":
    my_database = """
    CREATE TABLE IF NOT EXISTS my_database_task (
    id integer PRIMARY KEY

    )
    """