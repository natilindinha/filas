#listas para colocar as pessoas conforme onde se encaixam melhor
listinha = []
listona = []
listola = []

# funcao para mostrar as filas
def mostrar_filas():
    print('a lista de pessoas gravidas é ;')
    print(listona)
    print('a lista de pessoas idosas é ;')
    print(listola)
    print('a lista de pessoas não idosas e nem gravidas é ;')
    print(listinha)
    
# funcao para inserir na fila (nome, fila)
def inserir_na_fila():
    nome = input('digite seu nome: ')
    idoso = input(' você é idoso, tem mais de 60 anos :')
    idoso = idoso.lower()
    gravida = input('você está gravida ')
    gravida = gravida.lower()
    if idoso == 'sim':
        listola.append(nome)
    elif gravida == 'sim' :
        listona.append(nome)
    else:
        listinha.append(nome)
    
# funcao para remover da fila de acordo com a prioridade
def remover_da_fila():
    if len(listola) > 0:
        return listola.pop(0)
    elif len(listona) > 0:
        return listona.pop(0)
    elif len(listinha) > 0:
        return listinha.pop(0)

#menu
rodando = True
while rodando:

    print("1 - Mostrar as filas")
    print("2 - inserir na fila")
    print("3 - remover da fila")
    print("4 - Sair")

    opcao = int(input("Digite uma opção: "))

    if opcao == 4:
        rodando = False
    elif opcao == 1:
        mostrar_filas()
    elif opcao == 2:
        inserir_na_fila()
    elif opcao == 3:
        removido = remover_da_fila()
        print('Próximo: ', removido)
    else :
        print('essa opção não existe')
