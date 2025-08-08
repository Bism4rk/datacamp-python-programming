import numpy as np

def has_docstring(func):
  """Check to see if the function 
  `func` has a docstring.

  Args:
    func (callable): A function.

  Returns:
    bool
  """
  return func.__doc__ is not None

def load_and_plot_data():
  """Load and plot the data."""
  data = load_data() # type: ignore
  plot_data(data) # type: ignore

def as_2D(data):
  """Convert the data to a 2D array."""
  return np.array(data).reshape(-1, 2)

def log_product(a, b):
  result = a * b
  print(f"Product: {result}")
  return result

# Call has_docstring() on the load_and_plot_data() function
ok = has_docstring(load_and_plot_data)

if not ok:
  print("load_and_plot_data() doesn't have a docstring!")
else:
  print("load_and_plot_data() looks ok")

# Call has_docstring() on the as_2D() function
ok = has_docstring(as_2D)

if not ok:
  print("as_2D() doesn't have a docstring!")
else:
  print("as_2D() looks ok")

# Call has_docstring() on the log_product() function
ok = has_docstring(log_product)

if not ok:
  print("log_product() doesn't have a docstring!")
else:
  print("log_product() looks ok")

'''
O código acima demonstra como funções podem ser passadas como argumentos em Python. A função `has_docstring()` é um exemplo de função que aceita outra função como argumento e verifica se ela possui uma docstring.
'''