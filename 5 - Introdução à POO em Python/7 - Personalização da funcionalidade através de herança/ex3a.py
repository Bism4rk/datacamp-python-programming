class Player:
    MAX_POSITION = 10

    def __init__(self):
      self.position = 0

    def move(self, steps):
      if self.position + steps < Player.MAX_POSITION:
        self.position += steps 

      else:
        self.position = Player.MAX_POSITION      

# Create a Racer class inheriting from Player
class Racer(Player):
  # Create MAX_POSITION with a value of 15
  MAX_POSITION = 15
  
# Create a Player and a Racer objects
p = Player()
r = Racer()

print("p.MAX_POSITION = ", p.MAX_POSITION)
print("r.MAX_POSITION = ", r.MAX_POSITION)

'''
O código acima demonstra como criar uma hierarquia de classes em Python, onde a classe Racer herda da classe Player. Isso permite que a classe Racer tenha todas as funcionalidades da classe Player, além de suas próprias características específicas.
'''