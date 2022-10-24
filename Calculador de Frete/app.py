
def dimensoesobjeto():

    while True:

        try:
            altura = float(input('qual a altura do objeto?'))
        except ValueError:
            print('Você digitou um valor não numerico! tente novamente')
            continue
        if altura <= 0:
            print('Você digitou um valor menor ou igual a 0, tente novamente')
            continue

        try:
            comprimento = float(input('qual o comprimento do objeto?'))
        except ValueError:
            print('Você digitou um valor não numerico! tente novamente')
            continue
        if comprimento <= 0:
            print('Você digitou um valor menor ou igual a 0, tente novamente')
            continue

        try:
            largura = float(input('qual a largura do objeto?'))
        except ValueError:
            print('Você digitou um valor não numerico! tente novamente')
            continue
        if largura <= 0:
            print('Você digitou um valor menor ou igual a 0, tente novamente')
            continue
     
        volume = altura * comprimento * largura

        if volume < 1000:
            return 10

        elif 1000 <= volume < 10000:
            return 20

        elif 10000 <= volume < 30000:
         return 30

        elif 30000 <= volume < 100000:
           return 30
    
        elif volume >= 100000:
            print('não aceitamos um produto tão grande!')
            print('entre com o valor novamente!')

        

def pesoobjeto():
    
   while True:

    try:
        peso = float(input('qual o peso(Kg) do objeto?'))
        
        if peso <= 0.1:
            return 0.1
        
        elif 0.1 < peso <= 1:
            return 1.5
        
        elif 1 < peso <= 10:
            return 2.0
        
        elif 10 <= peso <= 30:
            return 3.0
        
        elif peso > 30:
            print('não aceitamos um produto tão pesado, entre com o valor novamente')
            continue
    except ValueError:
        print('Você digitou um valor não numerico! tente novamente')
        continue
    break
       
def rotaobjeto():
    print('Selecione a rota desejada:')
    print('RS - De Rio de Janeiro até São Paulo')
    print('SR - De São Paulo até Rio de Janeiro')
    print('BS - De Brasília até São Paulo')
    print('SB - De São Paulo até Brasília')
    print('BR - De Brasília até Rio de Janeiro')
    print('RB - Rio de Janeiro até Brasília')
    while True:
        rota = input('Digite a rota desejada:')
        if rota == 'RS':
            return 1
        
        elif rota == 'SR':
            return 1
    
        elif rota == 'BS':
            return 1.2

        elif rota == 'SB':
            return 1.2

        elif rota == 'BR':
            return 1.5

        elif rota == 'RB':
            return 1.5
        
        else:
            print('Você digitou um código não presente na tabela, tente novamente!')
            continue

 
#-----------------------main-----------------------#
print('bem vindo a loja João Marcelo de Melo Bomfim')
dimensao = dimensoesobjeto()
peso = pesoobjeto()
rota = rotaobjeto()
total = dimensao * peso * rota
print(f'o preço do produto ficou da seguinte forma:{dimensao:.2f}R$ da dimensão, {peso:.2f}R$ do peso, {rota:.2f}R$ da rota, tendo como total a ser pago de {total:.2f}R$')
