
class Employee:
    def __init__ (self,id, name, position,salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"Employee({self.id}, {self.name}, {self.position}, {self.salary})"