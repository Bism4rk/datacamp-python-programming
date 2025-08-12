def returns(return_type):
  # Complete the returns() decorator
  def decorator(func):
    def wrapper(*args, **kwargs):
      result = []
      assert type(result) == return_type
      return result
    return wrapper
  return decorator
  
@returns(dict)
def foo(value):
  return value

try:
  print(foo([1,2,3]))
except AssertionError:
  print('foo() did not return a dict!')

'''
O código acima demonstra mais uma vez como criar um decorador que permite especificar o tipo de retorno esperado de uma função. O decorador utiliza uma asserção para verificar o tipo de retorno da função e, se não corresponder ao tipo esperado, levanta uma exceção.
'''