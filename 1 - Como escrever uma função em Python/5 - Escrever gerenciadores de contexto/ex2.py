import contextlib

@contextlib.contextmanager
def open_read_only(filename):
  """Open a file in read-only mode.

  Args:
    filename (str): The location of the file to read

  Yields:
    file object
  """
  read_only_file = open(filename, mode='r')
  # Yield read_only_file so it can be assigned to my_file
  yield read_only_file
  # Close read_only_file
  read_only_file.close()

with open_read_only('C:\\Users\\reich\\Downloads\\datacamp-python-programming\\1 - Como escrever uma função em Python\\5 - Escrever gerenciadores de contexto\\my_file.txt') as my_file:
  print(my_file.read())


'''
O código acima demonstra como criar um gerenciador de contexto personalizado para abrir um arquivo em modo somente leitura. A função `open_read_only()` usa o decorador `contextlib.contextmanager` para definir um gerenciador de contexto que abre um arquivo, permite que ele seja lido dentro do bloco `with`, e garante que o arquivo seja fechado corretamente após o uso. Isso é útil para garantir que os recursos sejam gerenciados adequadamente, evitando vazamentos de memória ou arquivos abertos desnecessariamente.
'''