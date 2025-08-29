from ex2 import Player

# Create Players p1 and p2
p1 = Player(9)
p2 = Player(5)

print("MAX_POSITION of p1 and p2 before assignment:")
# Print p1.MAX_POSITION and p2.MAX_POSITION
print(p1.MAX_POSITION)
print(p2.MAX_POSITION)

# Assign 7 to p1.MAX_POSITION
p1.MAX_POSITION = 7

print("MAX_POSITION of p1 and p2 after assignment:")
# Print p1.MAX_POSITION and p2.MAX_POSITION
print(p1.MAX_POSITION)
print(p2.MAX_POSITION)

'''
O código acima demonstra como a atribuição de um novo valor a um atributo de classe em uma instância afeta apenas essa instância e não as outras. Quando p1.MAX_POSITION é definido como 7, isso não altera o valor de MAX_POSITION para p2, que ainda é 10. Isso ilustra a diferença entre atributos de classe e atributos de instância em Python.
'''