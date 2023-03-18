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
    database_chosen = "my-database-for-task.db"
    my_database = """
    CREATE TABLE IF NOT EXISTS my_database_task (
    id integer PRIMARY KEY,
    produkt text NOT NULL,
    cena float NOT NULL,
    ile float NOT NULL,
    status VARCHAR(20),
    );
    """
    connection = create_connection(database_chosen)
    execute_sql(connection, my_database)
