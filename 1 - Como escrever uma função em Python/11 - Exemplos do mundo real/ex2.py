def counter(func):
  def wrapper(*args, **kwargs):
    wrapper.count += 1
    # Call the function being decorated and return the result
    return func
  # Set count to 0 to initialize call count for each new decorated function
  wrapper.count = 0
  # Return the new decorated function
  return wrapper

# Decorate foo() with the counter() decorator
@counter
def foo():
  print('calling foo()')
  
foo()
foo()

print('foo() was called {} times.'.format(foo.count))

'''
O código acima demonstra mais uma vez como usar decoradores em Python para modificar o comportamento de funções. O decorador `counter` é aplicado à função `foo`, permitindo que o número de vezes que a função foi chamada seja rastreado e impresso.
'''