from data_acces import database as db
import json


if __name__ == "__main__":
    with open('python_repo\enviroment\enviroment.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    table=db.get_table_data(data,"employees")
    print(table)
