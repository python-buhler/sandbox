# Constantes
LOCAL_FILE = 'credito.py'

# Variáveis
credito = '''id_vendedor,valor_emprestimos,quantidade_emprestimos,data
104271,448.0,1,20161208
21476,826.7,3,20161208
87440,313.6,3,20161208
15980,-8008.0,6,20161208
215906,2212.0,5,20161208
33696,2771.3,2,20161208
33893,2240.0,3,20161208
214946,-4151.0,18,20161208
123974,2021.95,2,20161208
225870,4039.0,2,20161208'''

# PASSO 1. CRIAR ARQUIVO FÍSICO
print("Escrita de dados em arquivo CSV - comma separated values \n")

with open (LOCAL_FILE , mode='w') as file :
    file.write(credito)

# PASSO 2. LER O ARQUIVO FÍSICO
print("Leitura de dados em arquivo CSV - comma separated values \n")

with open (LOCAL_FILE , mode='r', encoding='utf8' ) as conteudo :
    elementos_lista = []


    linha = conteudo.readline()
    cabecalho_elementos = linha.strip().split(sep=',')
    
    linha = conteudo.readline()
    while linha:

            elementos = linha.strip().split(sep=',')
            
            elementos_linha = {}
            elementos_linha[cabecalho_elementos[0]] = elementos[0]
            elementos_linha[cabecalho_elementos[1]] = elementos[1]
            elementos_linha[cabecalho_elementos[2]] = elementos[2]
            elementos_linha[cabecalho_elementos[3]] = elementos[3]

            elementos_lista.append(elementos_linha)
            
            linha = conteudo.readline()

for elementos_linha in elementos_lista:
  print(elementos_linha)
  print('valor: ', elementos_linha[cabecalho_elementos[1]], '(', type(elementos_linha[cabecalho_elementos[1]]),')')

print('\n') # caracter não imprimível - quebra de linha

# PASSO 3. USAR A FUNÇÃO MAP PARA CRIAR UMA LISTA COM OS VALORES DOS EMPRÉSTIMOS TRANSFOREMADOS EM FLOAT
print("Uso da função Map \n")

valores_emprestimos_lista = []

def converter_str_float(str): 
    valor = str[cabecalho_elementos[1]]
    str[cabecalho_elementos[1]] = float(str[cabecalho_elementos[1]])
    return (str)

elementos_lista_float = list(map(converter_str_float, elementos_lista))

for elementos_linha in elementos_lista_float:
  print(elementos_linha)
  print('valor: ', elementos_linha[cabecalho_elementos[1]], '(', type(elementos_linha[cabecalho_elementos[1]]),')')

print('\n') # caracter não imprimível - quebra de linha