import os
import sys
import pyodbc
from models.employee import Employee
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def _create_connection(db_parameters:list[str]):
    conn = None
    connection_string = f"""DRIVER={db_parameters['DRIVER']};SERVER={db_parameters['SERVER']};
                          DATABASE={db_parameters['DATABASE']};Trusted_Connection={db_parameters['Trusted_Connection']};"""
    try:
        conn = pyodbc.connect(connection_string)
        print("Connected to MySQL database")
    except pyodbc.Error as e:
        print(e)
    return conn

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

def get_table_data(conn_string, table_name:str):
    """ get data from a table in the database """
    try:
        conn=_create_connection(conn_string)
        if conn is None:
            raise Exception("Connection to the database failed.")
        cursor = conn.cursor()
        sql = f"SELECT * FROM {table_name}"
        cursor.execute(sql)
        rows = cursor.fetchall()

        employees = [
            Employee(row[0],row[1],row[2],row[3])
            for row in rows
        ]
    except pyodbc.Error as e:
        print(e)
        employees=[]
    finally:
        cursor.close()
        return employees

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
