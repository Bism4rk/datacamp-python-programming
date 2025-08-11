def run_n_times(n):
  """Define and return a decorator"""
  def decorator(func):
    def wrapper(*args, **kwargs):
      for i in range(n):
        func(*args, **kwargs)
    return wrapper
  return decorator

# Make print_sum() run 10 times with the run_n_times() decorator
@run_n_times(10)
def print_sum(a, b):
  print(a + b)
  
print_sum(15, 20)

# Use run_n_times() to create the run_five_times() decorator
run_five_times = run_n_times(5)

@run_five_times
def print_sum(a, b):
  print(a + b)
  
print_sum(4, 100)

# Modify the print() function to always run 20 times
print = run_n_times(20)(print)

print('What is happening?!?!')

'''
O código acima demonstra como criar um decorador com parâmetros em Python. Um decorador é uma função que modifica o comportamento de outra função. Neste caso, o decorador run_n_times() permite que uma função seja executada várias vezes, conforme especificado pelo argumento n. Isso é útil para casos em que você deseja repetir a execução de uma função sem ter que escrever o loop manualmente. A diferença entre o decorador com e sem argumentos é que há uma função adicional que recebe o argumento e o utiliza para personalizar o comportamento do decorador.
'''