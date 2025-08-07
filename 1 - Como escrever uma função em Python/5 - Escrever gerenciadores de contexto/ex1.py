import contextlib
import time

# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def timer():
  """Time the execution of a context block.

  Yields:
    None
  """
  start = time.time()
  # Send control back to the context block
  yield 
  end = time.time()
  print('Elapsed: {:.2f}s'.format(end - start))

with timer():
  print('This should take approximately 0.25 seconds')
  time.sleep(0.25)

'''
O código acima demonstra como criar um gerenciador de contexto personalizado em Python usando o decorador `contextlib.contextmanager`. A função `timer()` mede o tempo gasto dentro do bloco `with`. Quando o bloco é executado, ele imprime o tempo decorrido. Isso é útil para medir a performance de trechos de código, garantindo que o tempo seja medido corretamente, mesmo que ocorram exceções durante a execução.
'''