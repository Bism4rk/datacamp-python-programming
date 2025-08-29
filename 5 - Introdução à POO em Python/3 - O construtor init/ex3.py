# Define and initialize the Calculator class
class Calculator:
  def __init__(self, num_one, num_two):
    self.num_one = num_one
    self.num_two = num_two
  
  # Create the addition method
  def addition(self):
    return self.num_one + self.num_two
  
  # Create the subtraction method
  def subtraction(self):
    return self.num_one - self.num_two
  
  # Create the multiplication method
  def multiplication(self):
    return self.num_one * self.num_two   
  
'''
O código acima demonstra como criar uma classe de calculadora simples em Python. A classe possui um construtor __init__ que inicializa dois números e métodos para realizar operações matemáticas básicas, como adição, subtração e multiplicação. Isso ilustra como a POO pode ser usada para organizar e estruturar código de forma eficaz.
'''