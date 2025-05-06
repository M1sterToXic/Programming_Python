class Employee:
    """Базовый класс для всех сотрудников"""
    emp_count = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print("Всего сотрудников: %d"%Employee.emp_count)

    def display_employee(self):
        print("Имя: {}. Зарплата: {}".format(self.name, self.salary ))

"""Это создаст 1 обЪект класса Employee"""
emp1 = Employee("Max", 5000)
emp2 = Employee("Dima", 2000)
emp1.display_employee()
emp2.display_employee()
print("Всего сотрудников: %d"%Employee.emp_count)
print(Employee.__doc__)

print(getattr(Employee, 'emp_count', False))
print(hasattr(Employee, 'emp_count'))
print(setattr(Employee, 'age', 23))
print(Employee.age)
print(hasattr(Employee, 'age'))
print(delattr(Employee, 'age'))
print(hasattr(Employee, 'age'))
print(Employee.__dict__)


