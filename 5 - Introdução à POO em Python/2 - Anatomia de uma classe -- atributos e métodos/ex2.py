class Employee:
  
  # Include a set_name method
  def set_name(self, new_name):
    self.name = new_name

emp = Employee()

# Use set_name() on emp to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')
print(emp.name)

'''
O código acima demonstra como definir e acessar atributos de instância em uma classe Python. A classe Employee possui um método set_name que permite definir o nome do empregado. Depois de criar uma instância da classe, podemos usar esse método para atribuir um nome ao empregado.
'''