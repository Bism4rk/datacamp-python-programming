# Create a Player class
class Player:
  
  # Create MAX_POSITION class attribute
  MAX_POSITION = 10
  
  # Add a constructor, setting position to zero
  def __init__(self):
    self.position = 0

# Create a player p and print its MAX_POSITION
p = Player()
print(p.MAX_POSITION)

'''
O código acima demonstra a diferença entre atributos de classe e atributos de instância em Python. Atributos de classe, como MAX_POSITION, são compartilhados entre todas as instâncias da classe, enquanto atributos de instância, como position, são específicos para cada objeto. Isso ilustra como a POO permite uma organização eficiente e flexível dos dados.
'''