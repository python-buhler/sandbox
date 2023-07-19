# TIPOS DE DADOS
# https://www.w3schools.com/python/python_datatypes.asp

print("+++ Tipos de dados +++", '\n')

# LISTA - LIST
print("+++ Lista +++")
lista_tabela = []

lista_linha1 = ['list1_Item1', "list1_Item2", "listItem3"]
lista_linha2 = ["list2_Item1", "list2_Item2", "listItem3"]
lista_linha3 = ["list3_Item1", "list3_Item2", "listItem3"]

lista_tabela.append(lista_linha1)
lista_tabela.append(lista_linha2)
lista_tabela.append(lista_linha3)

for lista_linha in lista_tabela:
    print(lista_linha)

print('\n')

print("+++ Dicionario +++")
# DICIONARIO - DICTIONARY
dicionario_tabela = {}

dicionario_tabela[1] = ["dicItem", "valor item 1", "dicItem", 99,"dicItem", 123.90]
dicionario_tabela[2] = ["dicItem", "valor item 2", "dicItem", 99, "dicItem", 123.90]

contador = len(dicionario_tabela)
while (contador > 0):
    print("Dic Item[",contador, "] :", dicionario_tabela[contador])
    contador = contador - 1

print('\n')