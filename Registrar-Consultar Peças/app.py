listapecas = []
#----------------Função CadastrarPeça----------------# 
def cadastrarpeca(co):
    while True:
        try:
            print('Você Selecionou a Opção de Cadastrar Peça!')
            print(f'O Codigo do Produto é {co}') #codigo recebe valor, iniciando com 1
            nome = input('Digite o Nome da Peça:') #úsuario digita nome do objeto

            fabricante = input('Digite o Fabricante da Peça:') #úsuario digita o fabricante do objeto

            preco = int(input('Digite o Preço da Peça:')) #usuario digita o preço do objeto

            dicionariopeca ={'codigo'   :    codigo,  #As variaveis (codigo, nome, fabricante e preço) é adiconada a um dicionario(dicionariopeca)
                            'nome'      :    nome, 
                            'fabricante':    fabricante,
                            'preço'     :    preco}

            listapecas.append(dicionariopeca.copy()) #dicionario peça é adicionado a lista de peças
        except ValueError:
            print(f'Voçê Digitou Um Valor Incorreto, Tente Novamente!')
        break




#----------------Função ConsultarPeça----------------#
def consultarpeca():
    print('Você Selecionou a Opção Consultar Peças!')

    while True: #laço de repetição
        try:
            res2 = int(input('Escolha a Opção Desejada\n'
                            '1- Consultar Todas as Peças\n'
                            '2- Consultar Peça por Código\n'
                            '3- Consultar Peça por Fabricante\n'
                            '4- Retornar\n'
                            '>>')) #input para o usuario digitar opção
            
            if res2 == 1:
                print('Você Escolheu Consultar Todas as Peças')
                for pecas in listapecas: 
                    for key , value in pecas.items():
                        print(f'{key} : {value}')

            
            elif res2 == 2:
                print('Você Escolheu Consultar Uma Peça por Código')
                entradac = int(input('Digite o Código desejado:'))
                for pecas in listapecas:
                    if pecas['codigo'] == entradac:
                        for key , value in pecas.items():
                            print(f'{key} : {value}')

            
            elif res2 == 3:
                print('Você Escolheu Consultar Uma Peça por Fabricante')
                entradaC = str(input('Digite o Fabricante da Peça:'))
                for pecas in listapecas:
                    if pecas['fabricante'] == entradaC:
                        for key , value in pecas.items():
                            print(f'{key} : {value}')
            

            elif res2 == 4:
                break


            else:
                print('você digitou uma opção inválida, tente novamente!')
            continue

        except ValueError:
            print('Você Digitou Uma Opção Inválida, Tente Novamente!')




#-----------------Função RemoverPeça-----------------#
def removerpeca():
    print('você selecionou a opção remover peças!')
    entradaR = input('Digite o Código da Peça Que Deseja Remover:')
    for pecas in listapecas:
        if (pecas['codigo'] == entradaR):
            listapecas.remove(pecas)
            



#-----------------Progama Principal-----------------#
print('Bem vindo ao Controle de Estoque da Bicicletaria do João Marcelo de Melo Bomfim')
codigo = 0
while True:
    try:
        res = int(input('digite a opção desejada:\n'
                        '1-Cadastrar Peça:\n'
                        '2- Consultar Peça:\n'
                        '3- Remover Peça:\n'
                        '4- Sair:\n'
                        '>>'))
        
        if res == 1:
            codigo = codigo + 1
            cadastrarpeca(codigo)


        elif res == 2:
            consultarpeca()


        elif res == 3:
            removerpeca()
        

        elif res == 4:
            print('progama finalizando...')
            break


        else:
            print('Você Digitou Uma Opção Inválida, Tente Novamente!')
            continue
    except ValueError:
        print('Você Digitou Um Valor Não Numerico, Tente Novamente!')
        continue