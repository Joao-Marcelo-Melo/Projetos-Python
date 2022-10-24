print('bem vindo a loja João Marcelo de Melo Bomfim')
preco = float(input('preço do produto desejado:'))
qtd = int(input('quantidade de produto desejado:'))
valortotal = preco * qtd

if (qtd < 9):
  print(f'o produto não terá desconto')
  print(f'o valor do produto será de {valortotal}')

elif (10<=qtd<=99):
  porcentagem = 5
  desconto = valortotal * (porcentagem/100)
  valorfinal = valortotal - desconto
  print(f'o valor sem desconto será de {valortotal:.2f}R$')
  print(f'o valor com desconto será de {valorfinal:.2f}R$ ({porcentagem}% de desconto)')

elif (100<=qtd<=999):
  porcentagem = 10
  desconto = valortotal * (porcentagem/100)
  valorfinal = valortotal - desconto
  print(f'o valor sem desconto será de {valortotal:.2f}R$')
  print(f'o valor com desconto será de {valorfinal:.2f}R$ ({porcentagem}% de desconto)')

elif (qtd>1000):
  porcentagem = 15
  desconto = valortotal * (porcentagem/100)
  valorfinal = valortotal - desconto
  print(f'o valor sem desconto será de {valortotal:.2f}R$')
  print(f'o valor com desconto será de {valorfinal:.2f}R$ ({porcentagem}% de desconto)')


