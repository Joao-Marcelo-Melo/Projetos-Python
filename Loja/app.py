print('bem vindo a loja do João Marcelo de Melo Bomfim')
valor_total = 0 #valor acumulativo
print('--------------------CARDÁPIO-------------------')
print('|Código|       Descrição              | Valor |')
print('|  100 |       Cachorro quente        | 9,00  |')
print('|  101 |       Cachorro Quente Duplo  | 11,00 |')
print('|  102 |       X-Egg                  | 12,00 |')
print('|  103 |       X-Salada               | 14,00 |')
print('|  104 |       X-Bacon                | 17,00 |')
print('|  105 |       X-Tudo                 | 17,00 |')
print('|  201 |       Regrigerante Lata      | 5,00  |')
print('|  202 |       Chá Gelado             | 5,00  |')
while True:
  codigo = input('digite o codigo do produto desejado:')
  if codigo == '100':
    valor_total = valor_total + 9  #valor acumulativo + o valor do produto na tabela(cachorro quente)
    print('você pediu um cachorro quente no valor de 9,00 ')

  elif codigo == '101':
    valor_total = valor_total + 11  #valor acumulativo + o valor do produto na tabela (cachorro quente duplo)
    print('você pediu um Cachorro Quente Duplo no valor de 11,00')

  elif codigo == '102':
    valor_total = valor_total + 12  #valor acumulativo + o valor do produto na tabela (X-egg)
    print('você pediu X-Egg no valor de 12,00')

  elif codigo == '103':
    valor_total = valor_total + 14   #valor acumulativo + o valor do produto na tabela (x-Salada)
    print('você pediu um X-Salada no valor de 14,00')

  elif codigo == '104':
    valor_total = valor_total + 17   #valor acumulativo + o valor do produto na tabela (X-Bacon)
    print('você pediu um X-Bacon no valor de 17,00')

  elif codigo == '105':
    valor_total = valor_total + 17    #valor acumulativo + o valor do produto na tabela (X-Tudo)
    print('você pediu um X-Tudo no valor de 17,00')

  elif codigo == '201':
    valor_total = valor_total + 5    #valor acumulativo + o valor do produto na tabela (Regrigerante)
    print('você pediu um Regrigerante Lata no valor de 5,00')

  elif codigo == '202':
    valor_total = valor_total + 5    #valor acumulativo + o valor do produto na tabela(Chá gelado)
    print('você pediu um Chá Gelado no valor de 5,00')

  else:
    print('você digitou um código incorreto, digite um código presente na tabela!')
    continue   #retorna para o inicio do while

  print('1 - sim')
  print('0 - não')
  resposta = input('deseja peidr mais alguma coisa?')
  if resposta == '1':
    continue   #retorna para o inicio do while

  else:
    print(f'O total a pagar é de {valor_total:.2f} Reais')
    break   #encerra o programa
