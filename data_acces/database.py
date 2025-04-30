import json
import pyodbc
from models.employee import Employee

def _create_connection():
    with open('python_repo\enviroment\enviroment.json', 'r', encoding='utf-8') as file:
        db_parameters = json.load(file)
    conn = None
    connection_string = f"""DRIVER={db_parameters['DRIVER']};SERVER={db_parameters['SERVER']};
                          DATABASE={db_parameters['DATABASE']};Trusted_Connection={db_parameters['Trusted_Connection']};"""
    try:
        conn = pyodbc.connect(connection_string)
        print("Connected to MySQL database")
    except pyodbc.Error as e:
        print(e)
    return conn

def update_table(sql:str, new_values:list):
    """ update a table in the database """
    try:
        conn=_create_connection()
        cursor = conn.cursor()
        cursor.execute(sql, new_values)
        conn.commit()
    except pyodbc.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def get_table_data(sql:str):
    """ get data from a table in the database """
    try:
        conn=_create_connection()
        if conn is None:
            raise Exception("Connection to the database failed.")
        cursor = conn.cursor()
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
        conn.close()
        return employees

def get_user_data(sql:str):
    """ get data from a table in the database """
    try:
        conn=_create_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
    except pyodbc.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        return rows

def insert_table(sql:str):
    """ insert data into a table in the database """
    try:
        conn=_create_connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except pyodbc.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#stworz wiecej rekodow w bazie danych, ktore bedzie mozna uzyc
#jako dane do statystki, regresji, bledu itp.
#uzytkownik powinine miec mozliowsc wyboru czy woli obrobic dane, czy tez wykonac operacje na bazie danych
#uzytkownik powininen miec mozliwosc uzyskania tych danych w postaci (np excela)
#cala ta logika powinna zostac przeniesiona do osobnej klasy, ktora bedzie odpowiedzialna za
#statystyki i regresje
#dobrze byloby stworzyc jakies wykresy, ktore pokaza regresje i bledy