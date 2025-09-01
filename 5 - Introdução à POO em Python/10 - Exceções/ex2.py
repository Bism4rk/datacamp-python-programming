class SalaryError(ValueError): 
  pass
class BonusError(SalaryError): 
  pass

class Employee:
  MIN_SALARY = 30000
  MAX_BONUS = 5000

  def __init__(self, name, salary = 30000):
    self.name = name    
    if salary < Employee.MIN_SALARY:
      raise SalaryError("Salary is too low!")      
    self.salary = salary
    
  # Raise exceptions  
  def give_bonus(self, amount):
    if amount > Employee.MAX_BONUS:
      raise BonusError("The bonus amount is too high!")  
        
    elif self.salary + amount <  Employee.MIN_SALARY:
      raise SalaryError("The salary after bonus is too low!")
      
    self.salary += amount

'''
O código acima demonstra como criar e usar exceções personalizadas em Python. Ele define duas exceções, SalaryError e BonusError, que são usadas na classe Employee para validar salários e bônus. Isso permite um tratamento de erros mais específico e informativo.
'''