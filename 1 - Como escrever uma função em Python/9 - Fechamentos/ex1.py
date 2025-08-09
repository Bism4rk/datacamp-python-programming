def return_a_func(arg1, arg2):
  def new_func():
    print('arg1 was {}'.format(arg1))
    print('arg2 was {}'.format(arg2))
  return new_func
    
my_func = return_a_func(2, 17)

print(my_func.__closure__ is not None)
print(len(my_func.__closure__) == 2)

# Get the values of the variables in the closure
closure_values = [
  my_func.__closure__[i].cell_contents for i in range(2)
]
print(closure_values == [2, 17])

'''
O código acima demonstra o conceito de fechamentos em Python. A função 'return_a_func' cria uma nova função 'new_func' que captura as variáveis 'arg1' e 'arg2' do escopo externo. Quando 'my_func' é chamada, ela tem acesso a esses valores, mesmo após 'return_a_func' ter sido executada. O valor da variável 'closure_values' é [2, 17], confirmando que os valores foram corretamente capturados. Fechamentos são uma maneira poderosa de preservar o estado em funções aninhadas, pois são tuplas que contêm referências a variáveis do escopo externo.
'''