class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
      
    # Add the __repr__() method  
    def __repr__(self):
        return f"Employee('{self.name}', {self.salary})"   

emp1 = Employee("Amar Howard", 30000)
print(repr(emp1))
emp2 = Employee("Carolyn Ramirez", 35000)
print(repr(emp2))

class Employee2:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
            
    # Add the __str__() method
    def __str__(self):
      emp_str = f"""Employee name: {self.name}
Employee salary: {self.salary}"""
      return emp_str

emp1 = Employee2("Amar Howard", 30000)
print(emp1)
emp2 = Employee2("Carolyn Ramirez", 35000)
print(emp2)

'''
O código acima demonstra como implementar os métodos especiais __repr__() e __str__() em uma classe Python. O método __repr__() é usado para fornecer uma representação não ambígua do objeto, que pode ser útil para depuração, enquanto o método __str__() é usado para fornecer uma representação legível por humanos do objeto.
'''