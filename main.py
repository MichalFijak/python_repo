from data_acces import datatransfer as dt

if __name__ == "__main__":

    userInput = input("Choose what you want to do:\n1. Add employee\n2. Update employee\n3. Show employees\n4. Show employee\n5. Exit\n")
    while userInput != "5":

        if userInput == "1":
            name = input("Enter employee name: ")
            salary = int(input("Enter employee salary: "))
            position = input("Enter employee position: ")
            dt.add_employee(name, salary=salary,position=position)

        elif userInput == "2":
            id = int(input("Enter employee id to update: "))
            position = input("Enter employee position: ")
            salary = int(input("Enter new employee salary: "))
            dt.update_employee(id,salary=salary,position=position)

        elif userInput == "3":
            employees=dt.get_all_employees()
            print("#############################")
            print("Employees:")
            for employee in employees:
                print(employee)
            print("#############################")

        elif userInput == "4":
            id = int(input("Enter employee id: "))
            employee=dt.get_employee(id)
            print("#############################")
            if employee:
                print(employee)
            else:
                print("Employee not found.")
            print("#############################")
        else:
            print("Invalid input. Please try again.")
        userInput = input("Choose what you want to do:\n1. Add employee\n2. Update employee\n3. Show employees\n4. Show employee\n5. Exit\n")