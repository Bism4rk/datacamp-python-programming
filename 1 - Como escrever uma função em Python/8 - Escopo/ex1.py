x = 50

def one():
  x = 10

def two():
  global x
  x = 30

def three():
  x = 100
  print(x)

for func in [one, two, three]:
  func()
  print(x)

'''
O código acima demonstra o conceito de escopo de variáveis em Python. A função 'one' cria uma variável local 'x', a função 'two' modifica a variável global 'x', e a função 'three' também cria uma variável local 'x' que é impressa. O valor de 'x' impresso após cada chamada de função reflete essas alterações. Os quatro valores impressos são 50, 30, 100, e 30.
'''