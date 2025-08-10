def print_before_and_after(func):
  def wrapper(*args):
    print('Before {}'.format(func.__name__))
    # Call the function being decorated with *args
    func(*args)
    print('After {}'.format(func.__name__))
  # Return the nested function
  return wrapper

@print_before_and_after
def multiply(a, b):
  print(a * b)

multiply(5, 10)

'''
O código acima demonstra como usar decoradores em Python para modificar o comportamento de funções. O decorador `print_before_and_after` é aplicado à função `multiply`, permitindo que mensagens sejam impressas antes e depois da execução da função.
'''