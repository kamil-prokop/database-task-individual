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


def add_produkt(connection, produkt):
    sql = '''INSERT INTO my_database_task(produkt, cena, ile, status)
                VALUES(?,?,?,?)'''
    cursor = connection.cursor()
    cursor.execute(sql, produkt)
    connection.commit()
    return cursor.lastrowid


def select_produkt_by_status(connection, status):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM my_database_task WHERE status=?", (status,))
    rows = cursor.fetchall()
    return rows


def select_all(connection, table):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    rows= cursor.fetchall()
    return rows

def select_where(connection, table, **query):
    cursor = connection.cursor()
    qs=[]
    values = ()
    for k, v in query.items():
        qs.append(f"{k}=?")
        values += (v,)
    q= " AND ".join(qs)
    cursor.execute(f"SELECT * FROM {table} WHERE {q}", values)
    rows = cursor.fetchall()
    return rows


def update(connection, table, id, **kwargs):
    parameters = [f"{k} = ?" for k in kwargs]
    parameters = ", ".join(parameters)
    values = tuple(v for v in kwargs.values())
    values += (id,)

    sql = f''' UPDATE {table}
                SET {parameters}
                WHERE id = ?'''
    
    try:
        cursor = connection.cursor()
        cursor.execute(sql, values)
        connection.commit()
        print("ok")
    except sqlite3.OperationalError as err:
        print(err)



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
    produkt = ("ser", "2.34", "2", "kupione")
    add_produkt(connection, produkt)

    select_where(connection, "my_database_task", status = "kupione")
    update(connection, "my-database-task", 1, status = "kupione")
    

    connection.commit()