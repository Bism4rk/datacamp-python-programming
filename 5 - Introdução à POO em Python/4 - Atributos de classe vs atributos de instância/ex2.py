class Player:
  MAX_POSITION = 10
  
  # Define a constructor
  def __init__(self, position):
    
    # Check if position is less than the class-level attribute value
    if position <= Player.MAX_POSITION:
      self.position = position
    
    # If not, set equal to the class-level attribute
    else:
      self.position = Player.MAX_POSITION

# Create a Player object, p, and print its MAX_POSITITON
p = Player(6)
print(p.MAX_POSITION)

'''
O código acima demonstra como usar atributos de classe e atributos de instância em Python. Atributos de classe, como MAX_POSITION, são compartilhados entre todas as instâncias da classe, enquanto atributos de instância, como position, são específicos para cada objeto. Isso ilustra como a POO permite uma organização eficiente e flexível dos dados.
'''