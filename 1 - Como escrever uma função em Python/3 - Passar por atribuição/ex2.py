'''
def add_column(values, df=pandas.DataFrame()):

  """Add a column of `values` to a DataFrame `df`.
  The column will be named "col_<n>" where "n" is
  the numerical index of the column.

  Args:
    values (iterable): The values of the new column
    df (DataFrame, optional): The DataFrame to update.
      If no DataFrame is passed, one is created by default.

  Returns:
    DataFrame
  """
  df['col_{}'.format(len(df.columns))] = values
  return df
'''
import pandas

# Use an immutable variable for the default argument
def better_add_column(values, df=None):
  """Add a column of `values` to a DataFrame `df`.
  The column will be named "col_<n>" where "n" is
  the numerical index of the column.

  Args:
    values (iterable): The values of the new column
    df (DataFrame, optional): The DataFrame to update.
      If no DataFrame is passed, one is created by default.

  Returns:
    DataFrame
  """
  # Update the function to create a default DataFrame
  if df is None:
    df = pandas.DataFrame()
  df['col_{}'.format(len(df.columns))] = values
  return df

'''
O código acima demonstra a importância de evitar o uso de objetos mutáveis como valores padrão para argumentos de funções em Python. No código original, uma DataFrame do pandas é usada como valor padrão, o que pode levar a comportamentos inesperados, pois o mesmo objeto DataFrame é compartilhado entre múltiplas chamadas da função. Isso pode resultar em modificações não intencionais do DataFrame. Já na função revisada, um valor imutável (None) é usado como padrão, e um novo DataFrame é criado dentro da função se nenhum DataFrame for fornecido. Isso garante que cada chamada da função trabalhe com um DataFrame separado, evitando efeitos colaterais indesejados.
'''