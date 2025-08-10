def print_return_type(func):
  # Define wrapper(), the decorated function
  def wrapper(*args, **kwargs):
    # Call the function being decorated
    result = func(*args, **kwargs)
    print('{}() returned type {}'.format(
      func.__name__, type(result)
    ))
    return result
  # Return the decorated function
  return wrapper
  
@print_return_type
def foo(value):
  return value
  
print(foo(42))
print(foo([1, 2, 3]))
print(foo({'a': 42}))

'''
O código acima demonstra como usar decoradores em Python para modificar o comportamento de funções. O decorador `print_return_type` é aplicado à função `foo`, permitindo que o tipo do valor retornado pela função seja impresso. Dentro da função, uma segunda função `wrapper` é definida, que envolve a chamada da função original e adiciona a lógica de impressão.
'''