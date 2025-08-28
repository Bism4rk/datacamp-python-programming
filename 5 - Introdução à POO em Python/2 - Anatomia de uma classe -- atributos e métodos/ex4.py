class Employee:
  def set_name(self, new_name):
    self.name = new_name

  def set_salary(self, new_salary):
    self.salary = new_salary 

  # Add a give_raise() method with amount as an argument
  def give_raise(self, amount):
    self.salary = self.salary + amount

# Create the emp object
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Print the salary
print(emp.salary)

# Give emp a raise of 1500
emp.give_raise(1500)
print(emp.salary)

'''
O código acima demonstra como definir e acessar atributos de instância em uma classe Python. A classe Employee possui métodos para definir o nome e o salário do empregado, bem como um método para aumentar o salário. Depois de criar uma instância da classe, podemos usar esses métodos para manipular os dados do empregado.
'''