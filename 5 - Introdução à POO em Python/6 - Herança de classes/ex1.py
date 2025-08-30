class Employee:
    MIN_SALARY = 30000    

    def __init__(self, name, salary=MIN_SALARY):
        self.name = name
        if salary >= Employee.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee.MIN_SALARY
        
    def give_raise(self, amount):
        self.salary += amount      
        
# Define a new class Manager inheriting from Employee
class Manager(Employee):
    # Add a keyword to leave this class empty
    pass

# Define a Manager object
mng = Manager('Debbie Lashko', 86500)

# Print mng's name
print(mng.name)

'''
O código acima demonstra como criar uma classe `Manager` que herda da classe `Employee`. A classe `Manager` não adiciona nenhum novo comportamento ou atributo, mas pode ser estendida no futuro. Um objeto `Manager` é criado e seu nome é impresso.
'''