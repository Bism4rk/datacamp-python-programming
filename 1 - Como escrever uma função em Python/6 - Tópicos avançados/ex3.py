import os
import contextlib

@contextlib.contextmanager
def in_dir(directory):
  """Change current working directory to `directory`,
  allow the user to run some code, and change back.

  Args:
    directory (str): The path to a directory to work in.
  """
  current_dir = os.getcwd()
  os.chdir(directory)

  # Add code that lets you handle errors
  try:
    yield
  # Ensure the directory is reset,
  # whether there was an error or not
  finally:
    os.chdir(current_dir)

'''
O código acima demonstra como tratar erros em um gerenciador de contexto em Python. Ele permite que você execute um bloco de código em um diretório específico e, se ocorrer um erro, o diretório de trabalho atual será restaurado. Isso é útil para garantir que seu código não afete o diretório de trabalho global, especialmente ao lidar com arquivos ou outros recursos que dependem do diretório atual.
'''