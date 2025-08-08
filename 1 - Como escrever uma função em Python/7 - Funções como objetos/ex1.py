from numpy import mean, std, minimum, maximum

def load_data():
    """Load the data from a file."""
    # Simulating data loading
    return [1, 2, 3, 4, 5]

def get_user_input():
    """Get the user's choice of function."""
    return input("Enter the function name (mean, std, minimum, maximum): ")

# Add the missing function references to the function map
function_map = {
  'mean': mean,
  'std': std,
  'minimum': minimum,
  'maximum': maximum
}

data = load_data()
print(data)

func_name = get_user_input()

# Call the chosen function and pass "data" as an argument
function_map[func_name](data)

'''
O código acima demonstra como funções podem ser tratadas como objetos de primeira classe em Python. Isso significa que você pode passar funções como argumentos, retorná-las de outras funções e armazená-las em estruturas de dados, como dicionários. No caso, o dicionário "function_map" armazena referências a funções do NumPy, permitindo que você escolha e chame uma função com base na entrada do usuário.
'''