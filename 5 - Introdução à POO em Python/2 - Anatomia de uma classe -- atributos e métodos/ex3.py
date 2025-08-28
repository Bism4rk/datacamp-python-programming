class Employee:
  def set_name(self, new_name):
    self.name = new_name
  
  # Add set_salary() method  
  def set_salary(self, new_salary):
    self.salary = new_salary 

emp = Employee()

# Use set_name to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Set the salary of emp to 50000
emp.set_salary(50000)

# Print the emp object's salary
print(emp.salary)

'''
O código acima demonstra como definir e acessar atributos de instância em uma classe Python. A classe Employee possui métodos set_name e set_salary que permitem definir o nome e o salário do empregado, respectivamente. Depois de criar uma instância da classe, podemos usar esses métodos para atribuir valores ao nome e ao salário do empregado.
'''