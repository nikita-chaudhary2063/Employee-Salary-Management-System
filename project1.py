'''
Employee Salary Management System
'''


class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.salary = basic_salary

    def calculate_salary(self, bonus=0, allowance=0):
        total_salary = self.salary + bonus + allowance
        return total_salary

    def show_details(self):
        print("Employee's name:", self.name)
        print("Employee's salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, basic_salary, department):
        super().__init__(name, basic_salary)
        self.department = department

    def calculate_salary(self, bonus=0, allowance=0):
        total_salary = super().calculate_salary(bonus, allowance)
        total_salary = total_salary + 5000
        return total_salary

    def show_details(self):
        super().show_details()
        print("Manager's department:", self.department)


employee1 = Employee("Nikita", 30000)
manager1 = Manager("Ram", 50000, "IT")

employee1.show_details()
print("Total salary:", employee1.calculate_salary(3000, 2000))

print()

manager1.show_details()
print("Total salary:", manager1.calculate_salary(5000, 2000))

