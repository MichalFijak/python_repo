import pyodbc


def create_connection(db_parameters:list[str]):
    conn = None
    try:
        conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-6U6QGK9\\SQLEXPRESS;DATABASE=python_database;Trusted_Connection=yes;")
        print("Connected to MySQL database")
    except pyodbc.Error as e:
        print(e)
    return conn

table_name="employees"
condition="id=1"
column_name="salary"
new_value="50000"

def get_table_data(conn, table_name:str):
    """ get data from a table in the database """
    try:
        cursor = conn.cursor()
        sql = f"SELECT * FROM {table_name}"
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except pyodbc.Error as e:
        print(e)
    finally:
        cursor.close()

def get_user_data(conn, table_name:str, condition:str):
    """ get data from a table in the database """
    try:
        cursor = conn.cursor()
        sql = f"SELECT * FROM {table_name} WHERE {condition}"
        cursor.execute(sql)
        rows = cursor.fetchall()
    except pyodbc.Error as e:
        print(e)
    finally:
        cursor.close()


def update_table(conn, table_name:str, column_name:str, new_value:str, condition:str):
    """ update a table in the database """
    try:
        cursor = conn.cursor()
        sql = f"UPDATE {table_name} SET {column_name} = ? WHERE {condition}"
        cursor.execute(sql, (new_value,))
        conn.commit()
    except pyodbc.Error as e:
        print(e)
    finally:
        cursor.close()

# def create_user_data(conn, table_name:str, column_name:str, new_value:str):
#     """ create a new user in the database """
#     try:
#         cursor = conn.cursor()
#         sql = f"INSERT INTO {table_name} ({column_name}) VALUES ()"
#         cursor.execute(sql, (new_value,))
#         conn.commit()
#         print("User created successfully")
#     except pyodbc.Error as e:
#         print(e)
#     finally:
#         cursor.close()

if __name__ == "__main__":
    db_parameters = [
    "DESKTOP-6U6QGK9\\SQLEXPRESS",
    "python_database"]
    conn = create_connection(db_parameters)
    if conn:
        data=get_user_data(conn, table_name, condition)
        if(data != None):
            update_table(conn, table_name, column_name, new_value, condition)
        # else:
            # create_user_data(conn, table_name, column_name, new_value, condition)
        data=get_table_data(conn, table_name)
        print(data)
        conn.close()
        print("Connection closed")
    else:
        print("Failed to create connection")
