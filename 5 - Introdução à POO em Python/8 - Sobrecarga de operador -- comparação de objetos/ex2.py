
class Phone:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return self.number == \
               other.number

pn = Phone(873555333)

class BankAccount:
  def __init__(self, number, balance=0):
    self.number, self.balance = number, balance
      
  def withdraw(self, amount):
    self.balance -= amount 

  # Modify to add a check for the class type
  def __eq__(self, other):
    return (self.number == other.number) and (type(self) == type(other))

acct = BankAccount(873555333)
pn = Phone(873555333)

# Check if the two objects are equal
print(acct == pn)

'''
O código acima demonstra como sobrecarregar o operador de igualdade (==) em uma classe Python. A classe BankAccount define o método __eq__ para comparar as contas com base no atributo number. Isso permite que as instâncias da classe BankAccount sejam comparadas diretamente usando o operador ==. Nesse caso, a comparação também verifica se os objetos são da mesma classe - o que é importante para garantir que estamos comparando objetos do mesmo tipo.
'''