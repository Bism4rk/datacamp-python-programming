from pandas import DataFrame

df = DataFrame({
    'y1_gpa': [3.0, 3.5, 2.8, 3.2],
    'y2_gpa': [3.1, 3.6, 2.9, 3.3],
    'y3_gpa': [3.2, 3.7, 3.0, 3.4],
    'y4_gpa': [3.3, 3.8, 3.1, 3.5]
})

"""
Código original:
# Standardize the GPAs for each year
df['y1_z'] = (df.y1_gpa - df.y1_gpa.mean()) / df.y1_gpa.std()
df['y2_z'] = (df.y2_gpa - df.y2_gpa.mean()) / df.y2_gpa.std()
df['y3_z'] = (df.y3_gpa - df.y3_gpa.mean()) / df.y3_gpa.std()
df['y4_z'] = (df.y4_gpa - df.y4_gpa.mean()) / df.y4_gpa.std()
"""

def standardize(column):
  """Standardize the values in a column.

  Args:
    column (pandas Series): The data to standardize.

  Returns:
    pandas Series: the values as z-scores
  """
  # Finish the function so that it returns the z-scores
  z_score = (column - column.mean()) / column.std()
  return z_score

# Use the standardize() function to calculate the z-scores
df['y1_z'] = standardize(df.y1_gpa)
df['y2_z'] = standardize(df.y2_gpa)
df['y3_z'] = standardize(df.y3_gpa)
df['y4_z'] = standardize(df.y4_gpa)

print(df[['y1_z', 'y2_z', 'y3_z', 'y4_z']])

'''
O código acima demonstra como aplicar o princípio DRY (Don't Repeat Yourself) em Python, criando uma função para padronizar os valores de GPA. No código original, a padronização era feita repetidamente para cada coluna de GPA, o que não é eficiente. A função `standardize` encapsula essa lógica, permitindo reutilização e manutenção mais fácil do código. Assim, qualquer alteração na lógica de padronização só precisa ser feita em um único lugar.
'''