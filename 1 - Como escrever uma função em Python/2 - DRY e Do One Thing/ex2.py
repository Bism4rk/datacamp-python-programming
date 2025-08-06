'''
def mean_and_median(values):
  """Get the mean and median of a sorted list of `values`

  Args:
    values (iterable of float): A list of numbers

  Returns:
    tuple (float, float): The mean and median
  """
  mean = sum(values) / len(values)
  values = sorted(values)
  midpoint = int(len(values) / 2)

  if len(values) % 2 == 0:
    median = (values[midpoint - 1] + values[midpoint]) / 2

  else:
    median = values[midpoint]

  return mean, median
'''

def mean(values):
  """Get the mean of a sorted list of values

  Args:
    values (iterable of float): A list of numbers

  Returns:
    float
  """
  # Write the mean() function
  mean = sum(values) / len(values)
  return mean

def median(values):
  """Get the median of a sorted list of values

  Args:
    values (iterable of float): A list of numbers

  Returns:
    float
  """
  # Write the median() function
  values = sorted(values)
  midpoint = int(len(values)/2)
  if len(values) % 2 == 0:
    median = (values[midpoint - 1] + values[midpoint]) / 2
  else:
    median = values[midpoint]
  return median

'''
O código acima demonstra como aplicar o princípio Do One Thing em Python, criando funções separadas para calcular a média e a mediana. Cada função tem uma única responsabilidade, o que facilita a compreensão e manutenção do código. A função `mean` calcula a média de uma lista de valores, enquanto a função `median` calcula a mediana. Isso permite que cada função seja reutilizada em diferentes contextos sem duplicação de código.
'''
