import stock # type: ignore

# Use the "stock('NVDA')" context manager
# and assign the result to the variable "nvda"
with stock('NVDA') as nvda:
  # Open "NVDA.txt" for writing as f_out
  with open('NVDA.txt', 'w') as f_out:
    for _ in range(10):
      value = nvda.price()
      print('Logging ${:.2f} for NVDA'.format(value))
      f_out.write('{:.2f}\n'.format(value))

'''
O código acima demonstra o uso de gerenciadores de contexto aninhados em Python. Ele permite que você trabalhe com recursos que precisam ser gerenciados, como arquivos ou conexões de rede, garantindo que sejam corretamente abertos e fechados. No exemplo, o gerenciador de contexto para a ação de "stock('NVDA')" é aninhado dentro do gerenciador de contexto para abrir o arquivo "NVDA.txt". Isso garante que ambos os recursos sejam gerenciados corretamente.
'''