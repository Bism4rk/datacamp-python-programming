def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`.

  # Add a Google style arguments section
  Args:
    content (str): The string to search.
    letter (str): The letter to search for.

  # Add a returns section
  Returns:
    int

  # Add a section detailing what errors might be raised
  Raises:
    ValueError: If `letter` is not a one-character string.
  """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])

'''
O código acima demonstra como escrever uma docstring detalhada para uma função Python. Ele inclui seções para argumentos, valor de retorno e possíveis erros que podem ser levantados. A docstring segue o estilo Google, que é amplamente utilizado na comunidade Python.
'''