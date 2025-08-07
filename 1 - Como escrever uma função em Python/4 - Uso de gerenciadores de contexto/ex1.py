# Open "alice.txt" and assign the file to "file"
with open('alice.txt') as file:
  text = file.read()

n = 0
for word in text.split():
  if word.lower() in ['cat', 'cats']:
    n += 1

print('Lewis Carroll uses the word "cat" {} times'.format(n))

'''
O código acima demonstra como usar um gerenciador de contexto em Python. Gerenciadores de contexto são usados para gerenciar recursos, como arquivos, garantindo que sejam corretamente abertos e fechados. Neste exemplo, o arquivo "alice.txt" é aberto, lido e fechado automaticamente ao final do bloco `with`, evitando a necessidade de chamar `file.close()` explicitamente. O código conta quantas vezes as palavras "cat" ou "cats" aparecem no texto lido.
'''