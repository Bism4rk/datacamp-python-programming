image = get_image_from_instagram() # type: ignore

# Time how long process_with_numpy(image) takes to run
with timer(): # type: ignore
  print('Numpy version')
  process_with_numpy(image) # type: ignore

# Time how long process_with_pytorch(image) takes to run
with timer(): # type: ignore
  print('Pytorch version')
  process_with_pytorch(image) # type: ignore


'''
O código acima demonstra o uso de gerenciadores de contexto para medir o tempo de execução de funções. A função `timer()` é um gerenciador de contexto que mede o tempo gasto dentro do bloco `with`. Neste exemplo, ele é usado para medir quanto tempo leva para processar uma imagem usando duas abordagens diferentes: uma com Numpy e outra com Pytorch. O uso do gerenciador de contexto garante que o tempo seja medido corretamente, mesmo que ocorram exceções durante a execução das funções.
'''