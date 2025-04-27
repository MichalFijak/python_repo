from data_acces import database as db

def update_employee(id, **kwargs):
    set_clause = ", ".join([f"{key} = ?" for key in kwargs.keys()])
    sql = f"UPDATE employees SET {set_clause} WHERE id = ?"
    try:
        values = list(kwargs.values())
        values.append(id) 
        db.update_table(sql, values) 
    except Exception as e:
        print(f"Error: {e}")
        return
    print("Employee updated successfully.")

def add_employee(name,**kwargs):
    columns = ", ".join(["name"] + list(kwargs.keys())) 
    placeholders = ", ".join(["?"] * (len(kwargs) + 1))  
    sql = f"INSERT INTO employees ({columns}) VALUES ({placeholders})"
    try:
        values = [name] + list(kwargs.values())
        db.update_table(sql, values)
    except Exception as e:
        print(f"Error: {e}")
        return
    print("Employee added successfully.")

def get_employee(id):
    sql = f"SELECT * FROM employees WHERE id = {id}"
    return db.get_user_data(sql)

def get_all_employees():
    sql = "SELECT * FROM employees"
    return db.get_table_data(sql)
