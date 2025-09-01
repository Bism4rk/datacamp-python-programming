# Modify the function to catch exceptions
def invert_at_index(x, ind):
  try:
    return 1/x[ind]
  except ZeroDivisionError:
    print("Cannot divide by zero!")
  except IndexError:
    print("Cannot divide by zero!")
  finally:
    print("Index out of range!")
 
a_list = [5,6,0,7]

# Works okay
print(invert_at_index(a_list, 1))

# Potential ZeroDivisionError
print(invert_at_index(a_list, 2))

# Potential IndexError
print(invert_at_index(a_list, 5))

'''
O código acima demonstra como lidar com exceções em Python usando blocos try, except e finally. Ele tenta inverter um valor em uma lista, mas pode encontrar erros de divisão por zero ou de índice fora do intervalo. As mensagens de erro apropriadas são exibidas quando essas exceções ocorrem.
'''