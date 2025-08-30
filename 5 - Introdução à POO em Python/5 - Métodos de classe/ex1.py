class Person:
  CURRENT_YEAR = 2024
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  # Add a class method decorator
  @classmethod
  # Define the from_birth_year method
  def from_birth_year(cls, name, birth_year):
    # Create age
    age = cls.CURRENT_YEAR - birth_year
    # Return the name and age
    return cls(name, age)

bob = Person.from_birth_year("Bob", 1990)

'''
O código acima demonstra como usar um método de classe para criar uma instância da classe Person a partir do ano de nascimento. A classe `Person` possui um método de classe chamado `from_birth_year`, que calcula a idade com base no ano de nascimento fornecido e retorna uma nova instância da classe `Person`.
'''