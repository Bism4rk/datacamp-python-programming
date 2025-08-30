class BetterDate:
  def __init__(self, year, month, day):
    self.year, self.month, self.day = year, month, day
    
  # Define a class method from_str
  @classmethod
  def from_str(cls, datestr):
    # Split the string at "-"
    parts = datestr.split("-")
    year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    # Return the class instance
    return cls(year, month, day)

# Create the xmas object      
xmas = BetterDate.from_str("2024-12-25") 
print(xmas.year)
print(xmas.month)
print(xmas.day)


'''
O código acima demonstra como usar um método de classe para criar uma instância da classe BetterDate a partir de uma string no formato "YYYY-MM-DD". A classe `BetterDate` possui um método de classe chamado `from_str`, que divide a string em partes e retorna uma nova instância da classe `BetterDate`.
'''