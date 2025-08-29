class Employee:
  def __init__(self, name, salary=0):
    self.name = name
    # Check if salary is positive
    if salary > 0:
      self.salary = salary
    else:
      self.salary = 0
      print("Invalid salary!")

  def give_raise(self, amount):
    self.salary += amount

  def monthly_salary(self):
    return self.salary / 12
      
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)

'''
O código acima demonstra como criar uma classe com um construtor __init__ que inicializa os atributos de instância. Ele também inclui métodos para aumentar o salário e calcular o salário mensal. O construtor __init__ é chamado automaticamente quando uma nova instância da classe é criada, o tornando essencial para a configuração inicial do objeto.
'''