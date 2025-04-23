import pyodbc
import json

def create_connection(db_parameters:list[str]):
    conn = None
    connection_string = f"""DRIVER={db_parameters['DRIVER']};SERVER={db_parameters['SERVER']};
                          DATABASE={db_parameters['DATABASE']};Trusted_Connection={db_parameters['Trusted_Connection']};"""
    try:
        conn = pyodbc.connect(connection_string)
        print("Connected to MySQL database")
    except pyodbc.Error as e:
        print(e)
    return conn


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
        return rows


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
    with open('python_repo\enviroment\enviroment.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        conn = create_connection(data)

    if conn:
        data=get_user_data(conn, "employees", "id=1")
        if(data != None):
            print(data)
        conn.close()
        print("Connection closed")
    else:
        print("Failed to create connection")
