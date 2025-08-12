def returns_dict(func):
  # Complete the returns_dict() decorator
  def wrapper(func):
    result = []
    assert type(result) == dict
    return result
  return wrapper
  
@returns_dict
def foo(value):
  return value

try:
  print(foo([1,2,3]))
except AssertionError:
  print('foo() did not return a dict!')

'''
O código acima demonstra como criar um decorador que garante que a função decorada retorne um dicionário. O decorador utiliza uma asserção para verificar o tipo de retorno da função e, se não for um dicionário, levanta uma exceção.
'''